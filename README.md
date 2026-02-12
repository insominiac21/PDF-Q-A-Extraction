# MentorBoxAI PDF Q/A Extraction Pipeline

## Overview


## Updated Architecture & Workflow

<div align="center">
  <h1>MentorBoxAI PDF Q/A Extraction Pipeline</h1>
  <img src="https://img.shields.io/badge/streamlit-ready-brightgreen" alt="Streamlit Ready" />
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="MIT License" />
</div>

---

## 🚀 Overview

Extract structured Q/A pairs from PDFs using MinerU, robust regex mining, and asset linking. Tables, formulas, images, and code blocks are handled as atomic blocks and linked to evidence in the output.

---

## 🛠️ Architecture & Workflow
graph TD
    PDF["PDF Input"] -->|MinerU API| ZIP["ZIP: Markdown + Assets"]
    ZIP -->|Normalize| MD["Normalized Markdown"]
    MD -->|"Regex Mining (Gemini)"| Patterns["Regex Patterns"]
    Patterns -->|Extract| QA["Q/A Pairs"]
    QA -->|Link| Assets["Tables, Images, Formulas, Code"]
    QA -->|Validate| JSON["Structured JSON Output"]
    JSON -->|UI| Streamlit["Streamlit App"]

## ✨ Features

- Deterministic MinerU Q/A extraction pipeline
- Robust regex mining (Gemini-assisted, fallback deterministic)
- Asset linking: tables, images, formulas, code blocks
- Evidence tracking and validation
- Modular backend, extensible for new asset types
- Modern Streamlit UI with custom dark theme
- Output: structured JSON in `output_json/` and `work/<pdf_hash>/final.json`

---

## ⚡ Quickstart

1. Clone the repo:
   ```bash
   git clone <repo-url>
   cd mentorboxai-pdf-parser
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add secrets securely:
   - For local/cloud use, create `.streamlit/secrets.toml`:
     ```toml
     mineru = "<YOUR_MINERU_API_KEY>"
     GEMINI_API_KEY = "<YOUR_GEMINI_API_KEY>"
     ```
   - Or use `.env` for local development:
     ```env
     mineru=<YOUR_MINERU_API_KEY>
     GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
     ```
   - `.streamlit/secrets.toml` is ignored by git for security.
4. UI & Theme:
   - All UI dependencies are in `requirements.txt` (`streamlit`, `streamlit_option_menu`, `Pillow`).
   - Custom theme via `.streamlit/config.toml`.
5. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 📦 Deployment

- Only core files are tracked for GitHub:
  - `streamlit_app.py` (main app)
  - `.streamlit/config.toml` (theme)
  - `requirements.txt` (dependencies)
  - `.env` (not tracked, add your keys)
  - `.gitignore` (excludes tests, sample ui, validation, logs, temp, output, .vscode, etc.)
- All unnecessary folders/files are excluded for a clean repo.
- UI dependencies: `streamlit`, `streamlit_option_menu`, `Pillow` (see `requirements.txt`).
- Custom theme via `.streamlit/config.toml`.
- For deployment, set secrets via .env or Streamlit webapp environment variables.

---

## 🧩 Module Responsibilities

- **mineru_runner**: Handles ZIP extraction and workspace setup
- **normalize_markdown**: Extracts atomic blocks and replaces with placeholders
- **mine_regex_patterns**: Mines regex templates (Gemini or fallback)
- **extract_qa_with_patterns**: Extracts Q/A pairs and links assets
- **Validation**: Checks extraction quality and triggers fallback if needed
- **Streamlit UI**: Orchestrates pipeline, handles upload, progress, and download

---

## 📝 Technical Details

- **MinerU-First Architecture**: All PDF parsing and markdown extraction is performed by the MinerU API, which returns a ZIP containing markdown, asset metadata, and block maps.
- **Regex-First, LLM-Assisted**: Q/A extraction is driven by regexes mined by Gemini. No LLM is used for extraction itself—only for pattern discovery.
- **Atomic Block Handling**: Tables, code, images, and formulas are replaced with placeholders during normalization and restored after extraction.
- **Heuristic Answer Pairing**: If no explicit answer marker is found, the parser pairs questions with the next plausible answer block, improving recall for implicit Q/A formats.
- **Extensible**: The system is designed to allow integration of standard Q/A extraction libraries if they become available.
- **API Key Management**: All keys are loaded from `.env` or `.streamlit/secrets.toml`.

---

## 🛠️ Usage

1. Install dependencies from `requirements.txt`.
2. Add your MinerU and Gemini API keys to `.env` or `.streamlit/secrets.toml`.
3. Run `streamlit_app.py` for UI-based extraction.
4. Review and download final JSON outputs.

---

## 🏷️ Example Output

See `final_refined.json` and `final_refined_postprocessed.json` for sample outputs.

---

## 🧪 Troubleshooting

- If UI theme does not apply, ensure `.streamlit/config.toml` exists.
- If asset linking fails, check `block_maps.json` and extraction logs.
- For API errors, verify `.env` keys and network access.

---

## 📋 Limitations & Next Steps

- Further improvements to table extraction and linking
- Enhanced validation and fallback logic
- Support for additional asset types and Q/A formats

---

## 📄 License

MIT License
