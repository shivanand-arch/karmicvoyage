"""
Resume text extraction from PDFs, DOCX, and TXT files.
Handles image-based PDFs with OCR fallback.
"""

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


def extract_text_from_pdf(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from a PDF file. Falls back to OCR if needed."""
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


def extract_text(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from any supported resume file."""
    ext = Path(file_path).suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path, max_chars)
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


def extract_resumes_from_zip(uploaded_file) -> dict:
    """
    Extract resume texts from an uploaded ZIP file.
    Returns dict of {archive_relative_path: text} (paths use / so nested files stay unique).
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
                text = extract_text(file_path)

                rel_path = os.path.relpath(file_path, extract_root).replace(os.sep, "/")
                if len(text.strip()) > 20:
                    resumes[rel_path] = text
                else:
                    failed.append(rel_path)

    return resumes, failed


def extract_text_from_uploaded_file(uploaded_file) -> str:
    """Extract text from a single uploaded file (PDF/DOCX/TXT)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return extract_text(file_path)
