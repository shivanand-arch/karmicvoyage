# Exotel Resume Screener

AI-powered resume screening tool for Exotel's hiring team. Upload JDs + resume ZIPs, get ranked Excel output with scores across role-specific evaluation dimensions.

## Supported Roles

- **Backend Engineer** (SE-1 to Sr. EM) — Backend depth, scale, ownership, GenAI, tech stack fit
- **Sales Manager** — Hunter mindset, solution selling, multi-threading, AI-first selling
- **SDR** — Outbound ownership, funnel metrics, qualification depth, technical curiosity
- **Chief of Staff** — Strategic thinking, execution & ops, cross-functional, domain fit
- **Engineering Manager (GenAI)** — Backend depth, GenAI expertise, leadership, tech stack

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

**System dependency for OCR (optional, for image-based PDFs):**

```bash
# macOS
brew install tesseract poppler

# Ubuntu/Debian
sudo apt-get install tesseract-ocr poppler-utils
```

### 2. Set API key

Either set environment variable:
```bash
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

Or paste it in the app sidebar when you run it.

### 3. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## How to Use

1. **Select a role framework** from the dropdown (Backend, Sales, SDR, etc.)
2. **Provide the JD** — paste text or upload a PDF/DOCX
3. **Upload a ZIP** containing resume files (PDF, DOCX, or TXT)
4. **Click "Evaluate & Rank"** — the tool will:
   - Extract text from each resume
   - Score each candidate across role-specific dimensions using Claude
   - Rank by weighted total score
   - Generate a formatted Excel with conditional coloring
5. **Download the Excel** with full rankings

## Deployment Options

### Streamlit Cloud (Free, easiest)
1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → Deploy
4. Add `ANTHROPIC_API_KEY` as a secret

### Railway / Render
1. Push to GitHub
2. Connect repo on Railway or Render
3. Set start command: `streamlit run app.py --server.port $PORT`
4. Add `ANTHROPIC_API_KEY` as env var

### Docker
```dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y tesseract-ocr poppler-utils
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## Adding New Role Frameworks

Edit `frameworks.py` and add a new entry to the `FRAMEWORKS` dict:

```python
"Your New Role": {
    "description": "Brief description",
    "dimensions": {
        "dimension_name": "What this dimension measures...",
    },
    "weights": {
        "dimension_name": 0.20,  # Must sum to 1.0
    },
    "context": "Role-specific context for the AI evaluator...",
}
```

The app will automatically pick up the new framework.

## Cost Estimate

Each resume evaluation = ~1 API call (~2K input + 1K output tokens)
- Sonnet: ~$0.01 per resume (~₹1)
- Opus: ~$0.10 per resume (~₹8)

100 resumes with Sonnet ≈ $1 (₹85)

## Architecture

```
app.py                  — Streamlit UI + orchestration
frameworks.py           — Evaluation frameworks (dimensions, weights, prompts)
resume_processor.py     — PDF/DOCX/TXT text extraction + OCR
excel_generator.py      — Formatted Excel output generation
```
