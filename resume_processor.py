"""
Resume text extraction from PDFs, DOCX, and TXT files.
Handles image-based PDFs with OCR fallback.
"""

import os
import io
import zipfile
import tempfile
from pathlib import Path

import pdfplumber

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
        text = ""

    # If pdfplumber got very little text, try OCR
    if len(text.strip()) < 50 and HAS_OCR:
        try:
            images = convert_from_path(file_path, dpi=200)
            text = "\n".join(pytesseract.image_to_string(img) for img in images)
        except Exception:
            pass

    return text[:max_chars]


def extract_text_from_docx(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from a DOCX file."""
    if not HAS_DOCX:
        return ""
    try:
        doc = docx.Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)
        return text[:max_chars]
    except Exception:
        return ""


def extract_text_from_txt(file_path: str, max_chars: int = 4000) -> str:
    """Extract text from a plain text file."""
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()[:max_chars]
    except Exception:
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


def extract_resumes_from_zip(uploaded_file) -> dict:
    """
    Extract resume texts from an uploaded ZIP file.
    Returns dict of {filename: text}
    """
    resumes = {}
    failed = []

    with tempfile.TemporaryDirectory() as tmpdir:
        # Save uploaded file to disk
        zip_path = os.path.join(tmpdir, "resumes.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract ZIP
        extract_dir = os.path.join(tmpdir, "extracted")
        with zipfile.ZipFile(zip_path, "r") as z:
            z.extractall(extract_dir)

        # Walk through extracted files
        for root, dirs, files in os.walk(extract_dir):
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

                if len(text.strip()) > 20:
                    resumes[fname] = text
                else:
                    failed.append(fname)

    return resumes, failed


def extract_text_from_uploaded_file(uploaded_file) -> str:
    """Extract text from a single uploaded file (PDF/DOCX/TXT)."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return extract_text(file_path)
