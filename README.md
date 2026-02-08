# MentorBoxAI PDF Q/A Extraction Pipeline

## Overview


## Updated Architecture & Workflow

### High-Level Architecture Diagram

```
PDF (input)
   │
   ## Setup

   1. Clone the repo:
      ```bash
      git clone <repo-url>
      cd mentorboxai-pdf-parser
      ```
   2. Install dependencies:
      ```bash
      pip install -r requirements.txt
      ```
   3. Add `.env` file with your MinerU and Gemini API keys:
      ```env
      mineru=<YOUR_MINERU_API_KEY>
      GEMINI_API_KEY=<YOUR_GEMINI_API_KEY>
      ```
   4. UI & Theme:
      - All UI dependencies are in `requirements.txt` (`streamlit`, `streamlit_option_menu`, `Pillow`).
      - Custom theme is set via `.streamlit/config.toml` (auto-created, see sample).
      - UI inspired by `sample ui/app.py`.
   5. Run the Streamlit app:
      ```bash
      streamlit run streamlit_app.py
      ```

   ## Features

   - Deterministic MinerU Q/A extraction pipeline
   - Asset linking: tables, images, formulas, code blocks
   - Evidence tracking and validation
   - Modular backend, robust regex mining, minimal Gemini usage
   - Modern Streamlit UI with dark/light mode and custom theme
   - Output: structured JSON in `output_json/` and `work/<pdf_hash>/final.json`

## Deployment

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

## Troubleshooting

- If UI theme does not apply, ensure `.streamlit/config.toml` exists.
- If asset linking fails, check `block_maps.json` and extraction logs.
- For API errors, verify `.env` keys and network access.

## License

- MIT
   - Links tables, images, and formulas to Q/A pairs using asset placeholders.
   - Evidence and asset metadata are included in the output.

5. **Post-processing (Further Split & Answer Extraction)**
   - Further splits Q/A pairs for granularity.
   - Extracts answers from question blocks if missing.
   - Ensures high-quality, structured JSON output.

6. **Validation & UI (Streamlit App)**
   - Streamlit app provides UI for PDF upload, pipeline execution, and JSON review/download.
   - Handles errors, cache, and provides download links for final outputs.


## Key Features


## Usage
1. Install dependencies from `requirements.txt`.
2. Add your MinerU and Gemini API keys to `.env`.
3. Run `streamlit_app.py` for UI-based extraction.
4. Review and download final JSON outputs.


## Example Output
See `final_refined.json` and `final_refined_postprocessed.json` for sample outputs.


## Module Responsibilities



## Technical Details

**MinerU-First Architecture**: All PDF parsing and markdown extraction is performed by the MinerU API, which returns a ZIP containing markdown, asset metadata, and block maps. Datalab is not used in this pipeline.

**Regex-First, LLM-Assisted**: Q/A extraction is driven by regexes mined by Gemini. No LLM is used for extraction itself—only for pattern discovery.

**Atomic Block Handling**: Tables, code, images, and formulas are replaced with placeholders during normalization and restored after extraction.

**Heuristic Answer Pairing**: If no explicit answer marker is found, the parser pairs questions with the next plausible answer block, improving recall for implicit Q/A formats.

**Extensible**: The system is designed to allow integration of standard Q/A extraction libraries if they become available.

**API Key Management**: All keys are loaded from `.env` using `python-dotenv`.


## Example .env

```
MINERU_API_KEY=your_mineru_key
GEMINI_API_KEY=your_gemini_key
```


## Limitations & Next Steps



## License
MIT License
