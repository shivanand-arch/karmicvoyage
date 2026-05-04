"""Tests that pin the prompt-caching contract.

If a future refactor accidentally undoes the split or moves cache_control to
the wrong block, these fail loudly. They run without an Anthropic API key.
"""

import os
import sys
import unittest
from unittest.mock import MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from frameworks import FRAMEWORKS, build_evaluation_prompt_split, get_framework_names


JD = "We are hiring a senior backend engineer. Must know Python and distributed systems."
RESUME = "Jane Doe\nSenior Engineer at Acme\n10 years Python, built a distributed queue system."
FILENAME = "jane_doe.pdf"


class PromptSplitContractTests(unittest.TestCase):
    """The split must keep static content out of the per-resume block."""

    def test_returns_three_part_tuple(self):
        for name in get_framework_names():
            with self.subTest(framework=name):
                parts = build_evaluation_prompt_split(name, JD, RESUME, FILENAME)
                self.assertEqual(len(parts), 3, f"{name} did not return 3-tuple")
                for part in parts:
                    self.assertIsInstance(part, str)
                    self.assertGreater(len(part), 0)

    def test_system_text_excludes_resume_and_jd(self):
        """System block is cached forever; must not contain per-call content."""
        for name in get_framework_names():
            with self.subTest(framework=name):
                system_text, _, _ = build_evaluation_prompt_split(name, JD, RESUME, FILENAME)
                self.assertNotIn(RESUME, system_text, f"{name}: resume leaked into system")
                self.assertNotIn(JD, system_text, f"{name}: JD leaked into system")
                self.assertNotIn(FILENAME, system_text, f"{name}: filename leaked into system")

    def test_jd_block_contains_jd_not_resume(self):
        """JD block is cached per-batch; must contain the JD but not the resume."""
        for name in get_framework_names():
            with self.subTest(framework=name):
                _, jd_block, _ = build_evaluation_prompt_split(name, JD, RESUME, FILENAME)
                self.assertIn(JD, jd_block)
                self.assertNotIn(RESUME, jd_block, f"{name}: resume leaked into JD block")

    def test_resume_block_contains_resume_and_filename(self):
        for name in get_framework_names():
            with self.subTest(framework=name):
                _, _, resume_block = build_evaluation_prompt_split(name, JD, RESUME, FILENAME)
                self.assertIn(RESUME, resume_block)
                self.assertIn(FILENAME, resume_block)

    def test_system_text_contains_rubric_anchors(self):
        """The system block must carry the scoring rubric (the whole point of caching it)."""
        for name in get_framework_names():
            with self.subTest(framework=name):
                system_text, _, _ = build_evaluation_prompt_split(name, JD, RESUME, FILENAME)
                self.assertIn("SCORING DIMENSIONS", system_text)
                self.assertIn("VERDICT THRESHOLDS", system_text)
                self.assertIn("SCORING CALIBRATION", system_text)


class CacheControlWiringTests(unittest.TestCase):
    """The actual API call must place cache_control on system + JD blocks."""

    def test_evaluate_single_resume_sends_cache_control_on_system_and_jd(self):
        from eval_engine import evaluate_single_resume

        captured = {}

        def fake_create(**kwargs):
            captured.update(kwargs)
            mock_response = MagicMock()
            mock_response.content = [
                MagicMock(text='{"name":"Jane","current_role":"Engineer","yoe":10,"scores":{},'
                               '"key_strengths":[],"key_concerns":[],"evidence_summary":""}')
            ]
            mock_response.usage.input_tokens = 100
            mock_response.usage.cache_creation_input_tokens = 0
            mock_response.usage.cache_read_input_tokens = 0
            mock_response.usage.output_tokens = 50
            return mock_response

        fake_client = MagicMock()
        fake_client.messages.create = fake_create

        framework_key = next(iter(FRAMEWORKS.keys()))
        evaluate_single_resume(
            api_key="sk-test",
            model="claude-sonnet-4-6",
            framework_key=framework_key,
            jd_text=JD,
            filename=FILENAME,
            resume_text=RESUME,
            client=fake_client,
        )

        # System block is cached
        self.assertIn("system", captured)
        self.assertIsInstance(captured["system"], list)
        self.assertEqual(captured["system"][0]["cache_control"], {"type": "ephemeral"})
        self.assertIn("SCORING DIMENSIONS", captured["system"][0]["text"])

        # User message has 2 content blocks: JD (cached) + resume (not cached)
        user_content = captured["messages"][0]["content"]
        self.assertIsInstance(user_content, list)
        self.assertEqual(len(user_content), 2, "user message should have JD block + resume block")
        self.assertEqual(user_content[0]["cache_control"], {"type": "ephemeral"},
                         "JD block must have cache_control: ephemeral")
        self.assertNotIn("cache_control", user_content[1],
                         "resume block must NOT be cached (varies per call)")
        self.assertIn(JD, user_content[0]["text"])
        self.assertIn(RESUME, user_content[1]["text"])


class ErrorCategorisationTests(unittest.TestCase):
    """Error bucketing should keep the operator-visible breakdown actionable."""

    def test_categorises_known_buckets(self):
        from eval_engine import categorize_error

        cases = {
            "auth_error": [
                "API error: authentication_error: invalid x-api-key",
                "401 Unauthorized",
                "permission denied",
            ],
            "billing": [
                "credit balance too low",
                "billing issue: payment required (402)",
            ],
            "rate_limit": [
                "API error: rate_limit_error",
                "HTTP 429 Too Many Requests",
                "quota exceeded",
            ],
            "timeout": [
                "Request timed out after 60s",
                "504 Gateway Timeout",
            ],
            "parse_error": [
                "AI evaluation failed to parse",
                "JSONDecodeError: Expecting value",
            ],
            "network": [
                "Connection reset by peer",
                "DNS resolution failed",
            ],
            "other": [
                "",
                "something unexpected",
            ],
        }
        for expected, samples in cases.items():
            for s in samples:
                with self.subTest(expected=expected, msg=s):
                    self.assertEqual(categorize_error(s), expected)


if __name__ == "__main__":
    unittest.main()
