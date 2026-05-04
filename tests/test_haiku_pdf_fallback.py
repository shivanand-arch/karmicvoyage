"""
Tests for the Haiku PDF-mode rescue path in resume_processor.

The local extraction tiers (pdfplumber + OCR) handle the easy 90% of
resumes for free. Haiku rescues the remaining hard cases — but only
when an API key is present and the local tiers genuinely failed.
These tests pin both halves of that contract.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

# Make the repo root importable regardless of where pytest/unittest is invoked.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from resume_processor import (  # noqa: E402
    HAIKU_MODEL_ID,
    HAIKU_RESCUE_THRESHOLD_CHARS,
    extract_text_from_pdf,
    extract_text_via_haiku,
)


def _fake_pdf(text_per_page):
    """Build a MagicMock that pdfplumber.open() can return as a context manager."""
    pdf = MagicMock()
    pages = []
    for t in text_per_page:
        page = MagicMock()
        page.extract_text.return_value = t
        pages.append(page)
    pdf.pages = pages
    cm = MagicMock()
    cm.__enter__.return_value = pdf
    cm.__exit__.return_value = False
    return cm


class HaikuRescueTriggerTests(unittest.TestCase):
    """Threshold + api_key gating around the Haiku call."""

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        self.tmp.write(b"%PDF-fake-bytes-for-tests")
        self.tmp.close()
        self.path = self.tmp.name

    def tearDown(self):
        os.unlink(self.path)

    @patch("resume_processor.HAS_OCR", False)
    @patch("resume_processor.pdfplumber.open")
    @patch("resume_processor.extract_text_via_haiku")
    def test_fires_when_pdfplumber_returns_too_little(self, mock_haiku, mock_open):
        mock_open.return_value = _fake_pdf(["tiny"])
        mock_haiku.return_value = "fully transcribed resume text " * 20

        result = extract_text_from_pdf(self.path, api_key="sk-test")

        mock_haiku.assert_called_once()
        self.assertIn("transcribed resume", result)

    @patch("resume_processor.HAS_OCR", False)
    @patch("resume_processor.pdfplumber.open")
    @patch("resume_processor.extract_text_via_haiku")
    def test_skipped_without_api_key(self, mock_haiku, mock_open):
        mock_open.return_value = _fake_pdf(["tiny"])

        extract_text_from_pdf(self.path, api_key="")

        mock_haiku.assert_not_called()

    @patch("resume_processor.HAS_OCR", False)
    @patch("resume_processor.pdfplumber.open")
    @patch("resume_processor.extract_text_via_haiku")
    def test_skipped_when_local_extraction_is_sufficient(self, mock_haiku, mock_open):
        long_text = "x" * (HAIKU_RESCUE_THRESHOLD_CHARS + 100)
        mock_open.return_value = _fake_pdf([long_text])

        extract_text_from_pdf(self.path, api_key="sk-test")

        mock_haiku.assert_not_called()

    @patch("resume_processor.HAS_OCR", False)
    @patch("resume_processor.pdfplumber.open")
    @patch("resume_processor.extract_text_via_haiku")
    def test_does_not_replace_when_haiku_returns_less(self, mock_haiku, mock_open):
        local_text = "y" * 100  # under threshold, but non-trivial
        mock_open.return_value = _fake_pdf([local_text])
        mock_haiku.return_value = "short"  # shorter than local

        result = extract_text_from_pdf(self.path, api_key="sk-test")

        mock_haiku.assert_called_once()
        # local text was kept because Haiku gave us less
        self.assertIn("y" * 50, result)


class HaikuClientWiringTests(unittest.TestCase):
    """Verifies the Haiku call uses the expected model + PDF document block."""

    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
        self.tmp.write(b"%PDF-fake-bytes-for-tests")
        self.tmp.close()
        self.path = self.tmp.name

    def tearDown(self):
        os.unlink(self.path)

    def test_calls_anthropic_with_haiku_model_and_pdf_block(self):
        with patch("anthropic.Anthropic") as mock_cls:
            fake_block = MagicMock()
            fake_block.type = "text"
            fake_block.text = "hello world"
            fake_resp = MagicMock()
            fake_resp.content = [fake_block]
            mock_cls.return_value.messages.create.return_value = fake_resp

            result = extract_text_via_haiku(self.path, "sk-test")

            mock_cls.assert_called_once_with(api_key="sk-test")
            create_kwargs = mock_cls.return_value.messages.create.call_args.kwargs
            self.assertEqual(create_kwargs["model"], HAIKU_MODEL_ID)
            content = create_kwargs["messages"][0]["content"]
            doc_blocks = [b for b in content if b["type"] == "document"]
            self.assertEqual(len(doc_blocks), 1)
            self.assertEqual(doc_blocks[0]["source"]["media_type"], "application/pdf")
            self.assertEqual(result, "hello world")

    def test_returns_empty_when_no_api_key(self):
        with patch("anthropic.Anthropic") as mock_cls:
            result = extract_text_via_haiku(self.path, "")
            mock_cls.assert_not_called()
            self.assertEqual(result, "")

    def test_returns_empty_on_api_failure(self):
        with patch("anthropic.Anthropic") as mock_cls:
            mock_cls.return_value.messages.create.side_effect = RuntimeError("boom")
            result = extract_text_via_haiku(self.path, "sk-test")
            self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
