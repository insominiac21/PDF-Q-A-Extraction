"""
Backend module stubs for deterministic MinerU Q/A extraction pipeline
"""

# mineru_runner: handles ZIP extraction and workspace setup
def mineru_runner(pdf_bytes, pdf_hash, workspace):
    # Save PDF, run MinerU, unzip result
    # Return ZIP path and workspace
    pass

# bundle_resolver: resolves markdown, assets, and structured files
def bundle_resolver(workspace):
    # Locate primary markdown, assets dir, optional JSONs
    # Return DocumentBundle dict
    pass

# markdown_normalizer: extracts atomic blocks and replaces with placeholders
def markdown_normalizer(md_path, block_maps_path):
    import re
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    block_maps = {'tables': [], 'images': [], 'formulas': [], 'code': []}
    # Extract HTML tables
    table_matches = list(re.finditer(r'<table\b[^>]*>[\s\S]*?</table>', text))
    for i, m in enumerate(table_matches):
        block_maps['tables'].append({'id': f'T{i+1}', 'html': m.group(0)})
        text = text.replace(m.group(0), f'[[TABLE:T{i+1}]]')
    # Extract images
    img_matches = list(re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', text))
    for i, m in enumerate(img_matches):
        img_path = m.group(1)
        # Try to find caption after image
        caption_match = re.search(rf'{re.escape(m.group(0))}\s*\n?([^\n]*)', text)
        caption = caption_match.group(1).strip() if caption_match else ''
        block_maps['images'].append({'id': f'I{i+1}', 'path': img_path, 'caption': caption})
        text = text.replace(m.group(0), f'[[IMG:I{i+1}]]')
    # Extract block math (LaTeX)
    math_matches = list(re.finditer(r'\$\$[\s\S]*?\$\$', text))
    for i, m in enumerate(math_matches):
        block_maps['formulas'].append({'id': f'F{i+1}', 'latex': m.group(0)})
        text = text.replace(m.group(0), f'[[FORMULA:F{i+1}]]')
    # Extract fenced code blocks
    code_matches = list(re.finditer(r'```[\w+-]*\n[\s\S]*?\n```', text))
    for i, m in enumerate(code_matches):
        block_maps['code'].append({'id': f'C{i+1}', 'text': m.group(0)})
        text = text.replace(m.group(0), f'[[CODE:C{i+1}]]')
    # Save block_maps.json
    with open(block_maps_path, 'w', encoding='utf-8') as f:
        import json
        json.dump(block_maps, f, indent=2)
    # Save normalized text stream
    norm_txt_path = os.path.splitext(md_path)[0] + '_normalized.txt'
    with open(norm_txt_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return text, block_maps

# regex_miner: mines Q/A regex template from normalized text (no LLM)
def regex_miner(normalized_text):
    import re
    # Strict MinerU Q/A patterns
    q_pattern = r'^(?:#{1,6}\s*)?Q(?P<num>\d+)\.\s+(?P<qtext>.+)$'
    a_pattern = r'^Answer:\s*(?P<atext>.*)$'
    section_pattern = r'^#{1,6}\s*Section\b.*$'
    stop_conditions = ['next_question', 'next_section', 'eof']
    # Diagnostics
    q_matches = list(re.finditer(q_pattern, normalized_text, re.MULTILINE))
    a_matches = list(re.finditer(a_pattern, normalized_text, re.MULTILINE))
    coverage = len(q_matches)
    confidence = 1.0 if coverage > 0 else 0.0
    ruleset = {
        'question_start_patterns': [q_pattern],
        'answer_start_patterns': [a_pattern],
        'section_heading_pattern': section_pattern,
        'stop_conditions': stop_conditions,
        'atomic_blocks': ['html_table', 'image', 'block_math', 'code_fence'],
        'exclusions': ['captions_inside_tables', 'code_blocks'],
        'confidence': confidence,
        'diagnostics': {'coverage': coverage, 'false_positives': 0, 'notes': []}
    }
    return ruleset

# parser: applies ruleset to extract Q/A pairs and link assets
def parser(normalized_text, block_maps, ruleset):
    import re
    items = []
    q_regex = re.compile(ruleset['question_start_patterns'][0], re.MULTILINE)
    a_regex = re.compile(ruleset['answer_start_patterns'][0], re.MULTILINE)
    # Find all questions
    q_matches = list(q_regex.finditer(normalized_text))
    for idx, q_match in enumerate(q_matches):
        q_start = q_match.end()
        q_end = q_matches[idx+1].start() if idx+1 < len(q_matches) else len(normalized_text)
        block = normalized_text[q_start:q_end]
        # Find answer in block
        a_match = a_regex.search(block)
        answer = a_match.group('atext').strip() if a_match else ''
        question = q_match.group('qtext').strip()
        # Asset linking
        def find_asset_links(text, block_maps):
            table_tags = re.findall(r'\[\[TABLE:T(\d+)\]\]', text)
            img_tags = re.findall(r'\[\[IMG:I(\d+)\]\]', text)
            formula_tags = re.findall(r'\[\[FORMULA:F(\d+)\]\]', text)
            code_tags = re.findall(r'\[\[CODE:C(\d+)\]\]', text)
            tables = [block_maps['tables'][int(i)-1]['id'] if block_maps['tables'] and int(i)-1 < len(block_maps['tables']) else f'T{i}' for i in table_tags]
            images = [block_maps['images'][int(i)-1]['id'] if block_maps['images'] and int(i)-1 < len(block_maps['images']) else f'I{i}' for i in img_tags]
            formulas = [block_maps['formulas'][int(i)-1]['id'] if block_maps['formulas'] and int(i)-1 < len(block_maps['formulas']) else f'F{i}' for i in formula_tags]
            code = [block_maps['code'][int(i)-1]['id'] if block_maps.get('code') and int(i)-1 < len(block_maps['code']) else f'C{i}' for i in code_tags]
            return {'tables': tables, 'images': images, 'formulas': formulas, 'code': code}
        asset_links = find_asset_links(question + answer, block_maps)
        items.append({
            'id': f'Q{idx+1:03d}',
            'question': {'number': idx+1, 'text': question, 'page_start': None, 'page_end': None},
            'answer': {
                'text_markdown': answer,
                'tables': asset_links['tables'],
                'images': asset_links['images'],
                'math': asset_links['formulas'],
                'code': asset_links['code']
            },
            'evidence': {
                'source_span': {'start_char': q_match.start(), 'end_char': q_end},
                'matched_pattern': ruleset['question_start_patterns'][0]
            }
        })
    return items

# validator: validates extraction quality and triggers fallback if needed
def validator(items, ruleset):
    # Check questions_found, empty_answer_rate, outliers, monotonic numbering
    # Return issues and fallback triggers
    pass

# gemini_regex_helper: optional fallback for regex mining (never extracts answers)
def gemini_regex_helper(snippet, context):
    # Call Gemini for regex candidates only if confidence is low
    pass
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageOps
import os
import zipfile
import json
import requests
import re

def safe_unzip(zip_path, extract_dir, max_files=100, max_size=200*1024*1024):
    total_size = 0
    file_count = 0
    with zipfile.ZipFile(zip_path, 'r') as z:
        for info in z.infolist():
            fname = info.filename
            if '..' in fname or fname.startswith('/'):
                continue
            file_count += 1
            total_size += info.file_size
            if file_count > max_files or total_size > max_size:
                break
            z.extract(info, extract_dir)

def find_best_md(unzipped_dir):
    md_files = []
    for root, _, files in os.walk(unzipped_dir):
        for f in files:
            if f.endswith('.md'):
                md_files.append(os.path.join(root, f))
    if not md_files:
        return None
    return max(md_files, key=lambda p: os.path.getsize(p))

def normalize_markdown(md_path, block_maps_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    tables = re.findall(r'(\|\|.+\|\|)', text)
    images = re.findall(r'!\[.*?\]\((.*?)\)', text)
    formulas = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    for i, t in enumerate(tables):
        text = text.replace(t, f'[[TABLE:T{i+1}]]')
    for i, img in enumerate(images):
        text = text.replace(img, f'[[IMG:I{i+1}]]')
    for i, fmla in enumerate(formulas):
        text = text.replace(f'$$'+fmla+'$$', f'[[FORMULA:F{i+1}]]')
    block_maps = {'tables': tables, 'images': images, 'formulas': formulas}
    with open(block_maps_path, 'w', encoding='utf-8') as f:
        json.dump(block_maps, f)
    return text, block_maps

def mine_regex_patterns(text, gemini_api_key):
    try:
        from google import genai
    except ImportError:
        st.error("Gemini error: No module named 'google.generativeai'. Please install the 'google-generativeai' package.")
        return {}
    # Expanded prompt with detailed instructions, multiple Q/A examples, asset placeholder samples, and explicit fallback instructions
    prompt = (
        "You are an expert at mining regex patterns for extracting question/answer pairs from educational markdown. "
        "Your task: Given the following markdown, return only strict regex patterns for questions and answers. Patterns should match only true Q/A pairs, not headings or numbered items. "
        "Patterns should cover: explicit question blocks (e.g., 'Q1.', 'Question 2:'), answer blocks (e.g., 'Answer:', 'Solution:'), and ignore headings, instructions, or metadata. "
        "If you cannot mine unique patterns, provide strict fallback patterns for Q/A formats. "
        "For each pattern, provide a brief example. "
        "Do NOT return JSON or extract Q/A pairs—just list the regex patterns and examples as plain text. "
        "Examples: \n"
        "Question pattern: r'(Q\\d+\\.|Question \\d+:|Q\\d+:)'\nExample: 'Q1. What is linear programming?'\n"
        "Answer pattern: r'(Answer:|Solution:|A:)'\nExample: 'Answer: Linear programming is ...'\n"
        "Stop condition: End of section, new heading, or blank line.\n"
        "Exclusion: Ignore headings, instructions, code blocks, metadata, or irrelevant text.\n"
        "Fallback pattern: r'(Q\\d+\\.|Question \\d+:|Q\\d+:)' for questions, r'(Answer:|Solution:|A:)' for answers.\n"
        "Markdown: " + text
    )
    os.environ["GEMINI_API_KEY"] = gemini_api_key
    client = genai.Client()
    max_attempts = 2
    ruleset = {}
    gemini_text = None
    for attempt in range(max_attempts):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )
            gemini_text = response.text if hasattr(response, 'text') else str(response)
            # Extract regex patterns from Gemini's plain text output
            ruleset = {}
            q_match = re.search(r'Question pattern:.*?`([^`]+)`', gemini_text, re.DOTALL)
            a_match = re.search(r'Answer pattern:.*?`([^`]+)`', gemini_text, re.DOTALL)
            stop_match = re.search(r'Stop condition:.*?`([^`]+)`', gemini_text, re.DOTALL)
            excl_match = re.search(r'Exclusion:.*?`([^`]+)`', gemini_text, re.DOTALL)
            # Fallback patterns
            q_fallback = re.search(r'Fallback Question pattern:.*?`([^`]+)`', gemini_text, re.DOTALL)
            a_fallback = re.search(r'Fallback Answer pattern:.*?`([^`]+)`', gemini_text, re.DOTALL)
            if q_match:
                ruleset['question_start_patterns'] = [q_match.group(1)]
            elif q_fallback:
                ruleset['question_start_patterns'] = [q_fallback.group(1)]
            if a_match:
                ruleset['answer_start_patterns'] = [a_match.group(1)]
            elif a_fallback:
                ruleset['answer_start_patterns'] = [a_fallback.group(1)]
            if stop_match:
                ruleset['stop_conditions'] = [stop_match.group(1)]
            if excl_match:
                ruleset['exclusions'] = [excl_match.group(1)]
            # If Gemini returns any patterns, break
            if ruleset and (ruleset.get('question_start_patterns') or ruleset.get('answer_start_patterns')):
                break
            else:
                st.warning(f"Gemini mining attempt {attempt+1} failed. Retrying...")
                prompt += "\nIf you cannot mine unique patterns, provide robust fallback patterns for numbered lists, headings, bolded phrases, answer blocks, and asset placeholders."
        except Exception as e:
            # Handle Gemini 503 errors gracefully
            err_msg = str(e)
            if '503' in err_msg or 'UNAVAILABLE' in err_msg:
                st.warning(f"Gemini mining attempt {attempt+1} failed: Model overloaded (503). Skipping to fallback patterns.")
                with open('gemini_regex_log.txt', 'a', encoding='utf-8') as logf:
                    logf.write(f"\n--- Gemini attempt {attempt+1} FAILED (503) ---\n{err_msg}\n")
                break
            else:
                st.warning(f"Gemini mining attempt {attempt+1} failed: {err_msg}")
                with open('gemini_regex_log.txt', 'a', encoding='utf-8') as logf:
                    logf.write(f"\n--- Gemini attempt {attempt+1} FAILED ---\n{err_msg}\n")
                continue
    # Log Gemini response for debugging
    with open('gemini_regex_log.txt', 'a', encoding='utf-8') as logf:
        logf.write(f"\n--- Gemini attempt {attempt+1} ---\n{gemini_text}\n")
    return ruleset

def extract_qa_with_patterns(text, block_maps, ruleset):
    # More robust fallback patterns for question and answer detection
    def sanitize_pattern(p):
        # Remove inline/global flags (e.g., (?m), (?i)) not at start
        p = re.sub(r'\(\?[a-z]+\)', '', p)
        return p.strip()
    q_patterns = [sanitize_pattern(p) for p in (ruleset.get('question_start_patterns') or [
        r'(# Q\d+\.|# Q\d+|Q\d+\.|Q\d+\)|Q\d+|Question \d+|\d+\.|\d+\)|# QUESTION|# Question|# .+|Q:|Q\d+\))',
        r'(Q\d+\))',
        r'(Q\d+\.)',
        r'(Q\d+)',
        r'(\d+\))',
        r'(\d+\.)',
        r'(Question \d+)',
        r'(\nQ:)',
        r'(# QUESTION BANK:)',
        r'(# Quick Tasks)',
        r'(# Section [A-Z] .+)',
        r'(# Concepts and Metrics)',
        r'(# Practice Packet)',
        r'(# Solution:)',
        r'(# Ans:)',
        r'(# Answer:)',
        r'(# Table:)',
        r'(# Formula:)',
        r'(# Image:)',
        r'(# Code:)',
        r'(# .+)' # headings
    ])]
    a_patterns = [sanitize_pattern(p) for p in (ruleset.get('answer_start_patterns') or [
        r'(A:|Answer:|Solution:|# Solution:|# Answer:|# Solution|# Answer|# Ans:|Ans:|\nAnswer:|\nAns:|\nSolution:|\n# Ans:|\n# Answer:|\n# Solution:|\n# Answer)' # covers more answer formats
    ])]
    qa = []
    # Compile each pattern separately to avoid inline flag errors
    q_regexes = [re.compile(p, re.DOTALL) for p in q_patterns]
    a_regexes = [re.compile(p, re.DOTALL) for p in a_patterns]
    # Find all question starts
    q_starts = []
    for regex in q_regexes:
        q_starts.extend(list(regex.finditer(text)))
    q_starts = sorted(q_starts, key=lambda m: m.start())
    # If no question starts found, try splitting by 'Q' or numbered list manually
    if not q_starts:
        manual_qs = list(re.finditer(r'(Q\d+\)|Q\d+\.|Q\d+|Question \d+|\d+\)|\d+\.|# .+)', text))
        q_starts = manual_qs
    for idx, q_match in enumerate(q_starts):
        q_start = q_match.end()
        q_end = q_starts[idx+1].start() if idx+1 < len(q_starts) else len(text)
        block = text[q_start:q_end]
        # Find first answer match in block
        a_match = None
        for a_regex in a_regexes:
            a_match = a_regex.search(block)
            if a_match:
                break
        if a_match:
            a_start = a_match.end()
            a_end = len(block)
            answer = block[a_start:a_end].strip()
            question = q_match.group(0) + block[:a_match.start()].strip()
        else:
            # Try to split by heading or 'Solution' if present
            alt_a_match = re.search(r'(# Solution:|# Answer:|A:|Answer:|Solution:)', block)
            if alt_a_match:
                a_start = alt_a_match.end()
                answer = block[a_start:].strip()
                question = q_match.group(0) + block[:alt_a_match.start()].strip()
            else:
                answer = ''
                question = q_match.group(0) + block.strip()

        # Asset linking: find all asset placeholders in question/answer
        def find_asset_links(text):
            # Find all asset placeholders in text
            table_tags = re.findall(r'\[\[TABLE:T(\d+)\]\]', text)
            img_tags = re.findall(r'\[\[IMG:I(\d+)\]\]', text)
            formula_tags = re.findall(r'\[\[FORMULA:F(\d+)\]\]', text)
            return {
                'linked_tables': [int(i)-1 for i in table_tags],
                'linked_images': [int(i)-1 for i in img_tags],
                'linked_formulas': [int(i)-1 for i in formula_tags]
            }

        asset_links = find_asset_links(question + answer)
        qa.append({
            'question': question.strip(),
            'answer': answer,
            'linked_tables': asset_links['linked_tables'],
            'linked_images': asset_links['linked_images'],
            'linked_formulas': asset_links['linked_formulas']
        })
    return qa

# Example Streamlit usage (main logic)

import hashlib
from dotenv import load_dotenv

def main():
    st.title("MentorBoxAI PDF Q/A Extraction Pipeline (MinerU + Gemini)")
    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
    if not uploaded_pdf:
        st.info("Please upload a PDF to begin.")
        return

    pdf_bytes = uploaded_pdf.read()
    pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()
    workspace = os.path.join('work', pdf_hash)
    os.makedirs(workspace, exist_ok=True)
    pdf_path = os.path.join(workspace, 'input.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)
    output_dir = os.path.join('output_json')
    os.makedirs(output_dir, exist_ok=True)
    final_json_path = os.path.join(workspace, 'final.json')  # cache
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    input_name = os.path.splitext(uploaded_pdf.name)[0]
    output_json_path = os.path.join(output_dir, f'{input_name}_{timestamp}.json')

    # Cache clear option
    if os.path.exists(final_json_path):
        st.success("Cached result found.")
        with open(final_json_path, 'r', encoding='utf-8') as f:
            cached_json = f.read()
            st.json(json.loads(cached_json))
            st.download_button("Download Final JSON", cached_json, file_name='final.json')
        if st.button("Clear Cache for this PDF"):
            import shutil
            shutil.rmtree(workspace, ignore_errors=True)
            if os.path.exists(output_json_path):
                os.remove(output_json_path)
            st.warning("Cache cleared. Please re-upload the PDF.")
            st.stop()
        st.stop()

    from dotenv import load_dotenv
    load_dotenv()
    token = os.getenv("mineru")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not token:
        st.error("MinerU API token not found in .env.")
        st.stop()
    if not gemini_api_key:
        st.error("Gemini API key not found in .env.")
        st.stop()

    # ...existing pipeline logic...
    # Option menu (future: multi-page)
    selected = option_menu(
        menu_title=None,
        options=["Upload PDF", "Pipeline Status", "Download Output"],
        icons=["file-earmark-arrow-up", "gear", "download"],
        orientation="horizontal"
    )
    if selected == "Upload PDF":
        uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])
        if not uploaded_pdf:
            st.info("Please upload a PDF to begin.")
            return
        pdf_bytes = uploaded_pdf.read()
        pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()
        workspace = os.path.join('work', pdf_hash)
        os.makedirs(workspace, exist_ok=True)
        pdf_path = os.path.join(workspace, 'input.pdf')
        with open(pdf_path, 'wb') as f:
            f.write(pdf_bytes)
        output_dir = os.path.join('output_json')
        os.makedirs(output_dir, exist_ok=True)
        final_json_path = os.path.join(workspace, 'final.json')  # cache
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        input_name = os.path.splitext(uploaded_pdf.name)[0]
        output_json_path = os.path.join(output_dir, f'{input_name}_{timestamp}.json')
        # Cache clear option
        if os.path.exists(final_json_path):
            st.success("Cached result found.")
            with open(final_json_path, 'r', encoding='utf-8') as f:
                cached_json = f.read()
                st.json(json.loads(cached_json))
                st.download_button("Download Final JSON", cached_json, file_name='final.json')
            if st.button("Clear Cache for this PDF"):
                import shutil
                shutil.rmtree(workspace, ignore_errors=True)
                if os.path.exists(output_json_path):
                    os.remove(output_json_path)
                st.warning("Cache cleared. Please re-upload the PDF.")
                st.stop()
            st.stop()
        # Use session keys if available, else fallback to .env
        mineru_key = st.session_state.get('mineru_key', None)
        gemini_key = st.session_state.get('gemini_key', None)
        if not mineru_key or not gemini_key:
            from dotenv import load_dotenv
            load_dotenv()
            import os
            mineru_key = mineru_key or os.getenv("mineru")
            gemini_key = gemini_key or os.getenv("GEMINI_API_KEY")
        if not mineru_key:
            st.error("MinerU API key not found. Please enter it in the sidebar settings.")
            st.stop()
        if not gemini_key:
            st.error("Gemini API key not found. Please enter it in the sidebar settings.")
            st.stop()
        # ...existing pipeline logic...
        # (Keep all extraction, validation, and download logic unchanged)
        # After extraction, show download button and pipeline status
        st.success("Extraction complete. See Pipeline Status or Download Output.")
    elif selected == "Pipeline Status":
        st.info("Check extraction progress, validation, and asset linking.")
        # Optionally show logs, validation issues, asset summary
        # ...existing code...
    elif selected == "Download Output":
        st.info("Download the final structured JSON output.")
        # ...existing code...
    token = os.getenv("mineru")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not token:
        st.error("MinerU API token not found in .env.")
        st.stop()
    if not gemini_api_key:
        st.error("Gemini API key not found in .env.")
        st.stop()

    # Step 1: MinerU API - Upload and parse PDF
    st.info("Requesting MinerU upload URL...")
    batch_url = "https://mineru.net/api/v4/file-urls/batch"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    data = {"files": [{"name": uploaded_pdf.name}], "model_version": "vlm"}
    resp = requests.post(batch_url, headers=headers, json=data)
    if resp.status_code != 200 or resp.json().get("code") != 0:
        st.error(f"Failed to get upload URL: {resp.text}")
        st.stop()
    file_upload_url = resp.json()["data"]["file_urls"][0]
    batch_id = resp.json()["data"]["batch_id"]
    st.info("Uploading file to MinerU...")
    upload_resp = requests.put(file_upload_url, data=pdf_bytes)
    if upload_resp.status_code != 200:
        st.error(f"File upload failed: {upload_resp.text}")
        st.stop()
    st.info("Waiting for MinerU parsing result...")
    poll_url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    zip_url = None
    import time
    for _ in range(60):
        poll_resp = requests.get(poll_url, headers=headers)
        poll_data = poll_resp.json()
        if poll_resp.status_code == 200 and poll_data.get("code") == 0:
            results = poll_data["data"].get("extract_result", [])
            for result in results:
                state = result.get("state", "")
                if state == "done":
                    zip_url = result.get("full_zip_url")
                    break
                elif state == "failed":
                    st.error(f"Parsing failed: {result.get('err_msg', '')}")
                    st.stop()
        if zip_url:
            break
        st.info("Still processing MinerU...")
        time.sleep(2)
    if not zip_url:
        st.error("Parsing did not complete in time.")
        st.stop()
    st.info("Downloading MinerU ZIP result...")
    zip_path = os.path.join(workspace, 'mineru_result.zip')
    zip_resp = requests.get(zip_url)
    with open(zip_path, 'wb') as f:
        f.write(zip_resp.content)
    st.info("Unzipping MinerU result...")
    unzipped_dir = os.path.join(workspace, 'unzipped')
    os.makedirs(unzipped_dir, exist_ok=True)
    safe_unzip(zip_path, unzipped_dir)

    # Step 2: Find and normalize markdown
    st.info("Resolving markdown/assets/metadata...")
    md_path = find_best_md(unzipped_dir)
    if not md_path:
        st.error("No markdown file found in ZIP.")
        st.stop()
    # Rename original MinerU markdown with input filename and timestamp
    orig_md_newname = os.path.join(unzipped_dir, f'{input_name}_{timestamp}_mineru.md')
    try:
        os.rename(md_path, orig_md_newname)
        md_path = orig_md_newname
    except Exception:
        pass  # If file already renamed or error, continue
    block_maps_path = os.path.join(workspace, 'block_maps.json')
    normalized_text, block_maps = normalize_markdown(md_path, block_maps_path)

    # Step 3: Gemini regex mining and Q/A extraction
    st.info("Mining regex patterns for Q/A extraction with Gemini...")
    ruleset = mine_regex_patterns(normalized_text, gemini_api_key)
    gemini_log = None
    used_gemini = False
    if ruleset and (ruleset.get('question_start_patterns') or ruleset.get('answer_start_patterns')):
        used_gemini = True
        st.success("Gemini regex mining succeeded. Using Gemini patterns.")
        gemini_log = ruleset
    else:
        st.warning("Gemini failed to mine regex patterns. Using fallback patterns.")
        ruleset = {}
    st.info("Extracting Q/A pairs using regex patterns...")
    qa_items = extract_qa_with_patterns(normalized_text, block_maps, ruleset)
    # --- Post-process: further split Q/A and improve answer extraction ---
    def further_split_qa(qa_list):
        refined = []
        for idx, item in enumerate(qa_list):
            # Only keep Q/A pairs with non-empty answer and question
            if not item['question'] or not item['answer']:
                continue
            # Evidence tracking: find asset placeholders in question and answer
            evidence = []
            for tag in ['TABLE', 'IMG', 'FORMULA']:
                if f'[[{tag}:' in item['question'] or f'[[{tag}:' in item['answer']:
                    evidence.append({'type': tag.lower(), 'snippet': item['question'] + '\n' + item['answer']})
            refined.append({
                'question': item['question'],
                'answer': item['answer'],
                'linked_tables': item.get('linked_tables', []),
                'linked_images': item.get('linked_images', []),
                'linked_formulas': item.get('linked_formulas', []),
                'evidence': evidence,
                'meta': {'index': idx}
            })
        return refined

    qa_items_refined = further_split_qa(qa_items)
    final_refined = {
        'qa': qa_items_refined,
        'tables': block_maps['tables'],
        'images': block_maps['images'],
        'formulas': block_maps['formulas'],
        'validation': {},
        'gemini_log': gemini_log if used_gemini else None,
        'input_file': uploaded_pdf.name,
        'timestamp': timestamp
    }

    # --- Validation Layer ---
    def validate_final_json(final):
        issues = []
        for idx, qa in enumerate(final['qa']):
            if not qa['answer']:
                issues.append(f"Q/A #{idx}: Missing answer.")
            if not qa['question']:
                issues.append(f"Q/A #{idx}: Missing question.")
            if qa['linked_tables'] or qa['linked_images'] or qa['linked_formulas']:
                if not qa['evidence']:
                    issues.append(f"Q/A #{idx}: Asset linked but no evidence.")
        if not final['qa']:
            issues.append("No Q/A pairs extracted.")
        return issues

    validation_issues = validate_final_json(final_refined)
    final_refined['validation']['issues'] = validation_issues
    final_refined['validation']['used_gemini'] = used_gemini
    if validation_issues:
        st.warning(f"Validation issues found: {validation_issues}")

    # Step 4: Save and show output
    with open(final_json_path, 'w', encoding='utf-8') as f:
        json.dump(final_refined, f, indent=2)
    with open(output_json_path, 'w', encoding='utf-8') as f:
        json.dump(final_refined, f, indent=2)
    st.success("Final JSON ready (post-processed).")
    st.json(final_refined)
    st.download_button(
        "Download Final JSON",
        json.dumps(final_refined, indent=2),
        file_name=f'{pdf_hash}_{timestamp}.json'
    )
    st.info(f"Output saved to {output_json_path}")
    if not final_refined['qa']:
        st.warning("No Q/A pairs were found. The extraction logic may need further tuning for this document.")

if __name__ == "__main__":
    main()