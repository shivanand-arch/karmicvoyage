"""
Resume text extraction from PDFs, DOCX, and TXT files.
Handles image-based PDFs with OCR fallback, and unreadable PDFs with a
Claude Haiku PDF-mode fallback when an API key is provided.
"""

import base64
import logging
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

import pdfplumber

logger = logging.getLogger(__name__)

try:
    import docx
    HAS_DOCX = True
except ImportError:
    HAS_DOCX = False

try:
    from pdf2image import convert_from_path
    import pytesseract
    HAS_OCR = True
except ImportError:
    HAS_OCR = False

# Haiku rescue triggers when local extraction (pdfplumber + OCR) returns
# fewer than this many printable chars. Tuned to catch multi-page resumes
# that came back near-empty without firing on 1-pager PDFs that are just
# legitimately short.
HAIKU_RESCUE_THRESHOLD_CHARS = 200
HAIKU_MODEL_ID = "claude-haiku-4-5-20251001"


def extract_text_via_haiku(file_path: str, api_key: str, max_chars: int = 4000) -> str:
    """Last-resort PDF transcription via Claude Haiku 4.5 native PDF support.

    Used only when pdfplumber + OCR both yield <HAIKU_RESCUE_THRESHOLD_CHARS.
    Returns "" on any failure so the caller can fall back to whatever local
    text it already has.
    """
    if not api_key:
        return ""
    try:
        import anthropic
    except ImportError:
        logger.debug("anthropic package not available; skipping Haiku PDF rescue")
        return ""

    try:
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        b64_pdf = base64.standard_b64encode(pdf_bytes).decode("utf-8")
        client = anthropic.Anthropic(api_key=api_key)
        msg = client.messages.create(
            model=HAIKU_MODEL_ID,
            max_tokens=4096,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": b64_pdf,
                        },
                    },
                    {
                        "type": "text",
                        "text": (
                            "Transcribe this resume to plain text. Output only "
                            "the resume content — every name, contact detail, "
                            "role, company, date, education entry, and skill. "
                            "Preserve section structure (Experience, Education, "
                            "Skills, etc.) with blank lines between sections. "
                            "Do not summarise. Do not add commentary or markdown. "
                            "Begin output immediately with the transcribed text."
                        ),
                    },
                ],
            }],
        )
        text_parts = [b.text for b in msg.content if getattr(b, "type", "") == "text"]
        text = "\n".join(text_parts).strip()
        return text[:max_chars]
    except Exception as e:
        logger.warning("Haiku PDF rescue failed for %s: %s", file_path, e)
        return ""


def extract_text_from_pdf(file_path: str, max_chars: int = 4000, api_key: str = "") -> str:
    """Extract text from a PDF file. Tiered fallback: pdfplumber → OCR → Haiku."""
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
    except Exception as e:
        logger.warning(f"Failed to extract text from {file_path}: {e}")
        text = ""

    # If pdfplumber got very little text, try OCR
    if len(text.strip()) < 50 and HAS_OCR:
        try:
            images = convert_from_path(file_path, dpi=200)
            text = "\n".join(pytesseract.image_to_string(img) for img in images)
        except Exception as e:
            logger.debug("OCR fallback failed for %s: %s", file_path, e)

    # If both pdfplumber and OCR were inadequate, ask Haiku to transcribe.
    # Only fires when an API key is present and prior tiers underperformed.
    if len(text.strip()) < HAIKU_RESCUE_THRESHOLD_CHARS and api_key:
        haiku_text = extract_text_via_haiku(file_path, api_key, max_chars)
        if len(haiku_text.strip()) > len(text.strip()):
            logger.info(
                "haiku_rescue file=%s local_chars=%d haiku_chars=%d",
                os.path.basename(file_path),
                len(text.strip()),
                len(haiku_text.strip()),
            )
            return haiku_text

    return text[:max_chars]


def extract_text_from_docx(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from a DOCX file."""
    if not HAS_DOCX:
        return ""
    try:
        doc = docx.Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)
        return text[:max_chars]
    except Exception as e:
        logger.warning(f"Failed to extract text from {file_path}: {e}")
        return ""


def extract_text_from_txt(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from a plain text file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()[:max_chars]
    except Exception as e:
        logger.warning(f"Failed to extract text from {file_path}: {e}")
        return ""


def extract_text(file_path: str, max_chars: int = 4000, api_key: str = "") -> str:
    """Extract text from any supported resume file."""
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path, max_chars, api_key=api_key)
    elif ext == ".docx":
        return extract_text_from_docx(file_path, max_chars)
    elif ext in (".txt", ".text"):
        return extract_text_from_txt(file_path, max_chars)
    else:
        return ""


def _safe_extractall(zf: zipfile.ZipFile, dest_dir: str) -> None:
    """Extract ZIP members only under dest_dir (mitigates zip slip)."""
    dest_root = os.path.realpath(dest_dir)
    os.makedirs(dest_root, exist_ok=True)
    for member in zf.infolist():
        name = (member.filename or "").replace("\\", "/")
        if not name or name.endswith("/"):
            continue
        if name.startswith("/") or any(p == ".." for p in name.split("/")):
            logger.warning("Skipping unsafe ZIP member: %s", member.filename)
            continue
        dest_path = os.path.realpath(os.path.join(dest_root, *name.split("/")))
        try:
            if os.path.commonpath([dest_root, dest_path]) != dest_root:
                logger.warning("Skipping ZIP slip path: %s", member.filename)
                continue
        except ValueError:
            logger.warning("Skipping ZIP member (invalid path): %s", member.filename)
            continue
        parent = os.path.dirname(dest_path)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with zf.open(member, "r") as src, open(dest_path, "wb") as dst:
            shutil.copyfileobj(src, dst)


def extract_resumes_from_zip(uploaded_file, api_key: str = "") -> tuple:
    """
    Extract resume texts from an uploaded ZIP file.
    Returns (dict of {archive_relative_path: text}, list of failed paths).
    """
    resumes = {}
    failed = []

    with tempfile.TemporaryDirectory() as tmpdir:
        # Save uploaded file to disk
        zip_path = os.path.join(tmpdir, "resumes.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        extract_dir = os.path.join(tmpdir, "extracted")
        os.makedirs(extract_dir, exist_ok=True)
        extract_root = os.path.realpath(extract_dir)
        with zipfile.ZipFile(zip_path, "r") as z:
            _safe_extractall(z, extract_root)

        # Walk through extracted files
        for root, dirs, files in os.walk(extract_root):
            # Skip __MACOSX folders
            if "__MACOSX" in root:
                continue
            for fname in sorted(files):
                # Skip hidden files and __MACOSX artifacts
                if fname.startswith(".") or fname.startswith("._"):
                    continue
                ext = Path(fname).suffix.lower()
                if ext not in (".pdf", ".docx", ".txt", ".text"):
                    continue

                file_path = os.path.join(root, fname)
                text = extract_text(file_path, api_key=api_key)

                rel_path = os.path.relpath(file_path, extract_root).replace(os.sep, "/")
                if len(text.strip()) > 20:
                    resumes[rel_path] = text
                else:
                    failed.append(rel_path)

    return resumes, failed


def extract_text_from_uploaded_file(uploaded_file, api_key: str = "") -> str:
    """Extract text from a single uploaded file (PDF/DOCX/TXT)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return extract_text(file_path, api_key=api_key)


def extract_text_from_bytes(filename: str, data: bytes, max_chars: int = 4000, api_key: str = "") -> str:
    """Extract text from raw file bytes (used for Trakstar-downloaded resumes)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, filename)
        with open(file_path, "wb") as f:
            f.write(data)
        return extract_text(file_path, max_chars, api_key=api_key)
