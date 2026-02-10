import streamlit as st
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
    # Robust atomic block extraction for all table, formula, image, code types
    # Tables: Markdown, HTML, LaTeX
    tables = []
    # Markdown table (improved: must have header, separator, and at least one row)
    md_table_pattern = re.compile(
        r'(?:^|\n)'
        r'(\|(?:[^\n]*\|)+)\s*\n'  # header
        r'(\|[ \t:.-]+\|)\s*\n'     # separator
        r'((?:\|(?:[^\n]*\|)+\s*\n){1,})',  # at least one data row
        re.MULTILINE
    )
    for m in md_table_pattern.finditer(text):
        table_block = m.group(0)
        if table_block.strip() and table_block in text:
            tables.append(table_block)
            text = text.replace(table_block, f'[[TABLE:T{len(tables)}]]')
            print(f"[DEBUG] Markdown table detected and appended. Length: {len(table_block)}")

    # Improved HTML table regex: non-greedy, multiline, robust to whitespace
    html_table_pattern = re.compile(r'<table[\s\S]*?<\/table>', re.IGNORECASE)
    for m in html_table_pattern.finditer(text):
        table_block = m.group(0)
        if table_block.strip() and table_block in text:
            tables.append(table_block)
            text = text.replace(table_block, f'[[TABLE:T{len(tables)}]]')
            print(f"[DEBUG] HTML table detected and appended. Length: {len(table_block)}")

    # LaTeX tabular
    latex_table_pattern = re.compile(r'(\\begin\{tabular\}[\s\S]*?\\end\{tabular\})', re.MULTILINE)
    for m in latex_table_pattern.finditer(text):
        table_block = m.group(0)
        if table_block.strip() and table_block in text:
            tables.append(table_block)
            text = text.replace(table_block, f'[[TABLE:T{len(tables)}]]')
            print(f"[DEBUG] LaTeX table detected and appended. Length: {len(table_block)}")

    # Fallback: very permissive table pattern (for edge cases)
    fallback_table_pattern = re.compile(r'<table[\s\S]+?<\/table>', re.IGNORECASE)
    for m in fallback_table_pattern.finditer(text):
        table_block = m.group(0)
        if table_block.strip() and table_block not in tables and table_block in text:
            tables.append(table_block)
            text = text.replace(table_block, f'[[TABLE:T{len(tables)}]]')
            print(f"[DEBUG] Fallback HTML table detected and appended. Length: {len(table_block)}")

    # Formulas: inline, block, LaTeX env
    formulas = []
    # Inline LaTeX
    for m in re.finditer(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', text):
        formulas.append(m.group(0))
        text = text.replace(m.group(0), f'[[FORMULA:F{len(formulas)}]]')
    # Block LaTeX
    for m in re.finditer(r'\$\$(.+?)\$\$', text, re.DOTALL):
        formulas.append(m.group(0))
        text = text.replace(m.group(0), f'[[FORMULA:F{len(formulas)}]]')
    # LaTeX envs
    for m in re.finditer(r'(\\begin\{(equation|align|gather|multline)\*?\}[\s\S]*?\\end\{\2\*?\})', text):
        formulas.append(m.group(0))
        text = text.replace(m.group(0), f'[[FORMULA:F{len(formulas)}]]')

    # Images: Markdown, HTML, LaTeX
    images = []
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', text):
        images.append(m.group(0))
        text = text.replace(m.group(0), f'[[IMG:I{len(images)}]]')
    for m in re.finditer(r'<img\s+[^>]*src=["\"]([^"\"]+)["\"][^>]*>', text):
        images.append(m.group(0))
        text = text.replace(m.group(0), f'[[IMG:I{len(images)}]]')
    for m in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', text):
        images.append(m.group(0))
        text = text.replace(m.group(0), f'[[IMG:I{len(images)}]]')

    # Code blocks: fenced, indented, HTML, LaTeX
    codes = []
    for m in re.finditer(r'```(?:[a-zA-Z0-9]*)\n([\s\S]*?)```', text):
        codes.append(m.group(0))
        text = text.replace(m.group(0), f'[[CODE:C{len(codes)}]]')
    for m in re.finditer(r'(?:^|\n)(    .+(?:\n    .+)*)', text):
        codes.append(m.group(0))
        text = text.replace(m.group(0), f'[[CODE:C{len(codes)}]]')
    for m in re.finditer(r'<pre>([\s\S]*?)</pre>', text):
        codes.append(m.group(0))
        text = text.replace(m.group(0), f'[[CODE:C{len(codes)}]]')
    for m in re.finditer(r'\\begin\{verbatim\}([\s\S]*?)\\end\{verbatim\}', text):
        codes.append(m.group(0))
        text = text.replace(m.group(0), f'[[CODE:C{len(codes)}]]')

    # Captions
    captions = []
    for m in re.finditer(r'^(Figure|Fig\.|Table|Formula)\s+\d+\s*:\s+.+$', text, re.MULTILINE):
        captions.append(m.group(0))
        text = text.replace(m.group(0), f'[[CAPTION:K{len(captions)}]]')

    # Section heading
    sections = []
    for m in re.finditer(r'^#{1,6}\s*Section\b.*$', text, re.MULTILINE):
        sections.append(m.group(0))

    block_maps = {
        'tables': tables,
        'images': images,
        'formulas': formulas,
        'codes': codes,
        'captions': captions,
        'sections': sections
    }
    print(f"[DEBUG] block_maps before JSON dump: {block_maps}")
    with open(block_maps_path, 'w', encoding='utf-8') as f:
        json.dump(block_maps, f)
    print(f"[DEBUG] block_maps after JSON dump: {block_maps}")
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
                model="gemini-2.0-flash",
                # model="gemini-3-flash-preview",
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
        r'(# .+)'
    ])]
    a_patterns = [sanitize_pattern(p) for p in (ruleset.get('answer_start_patterns') or [
        r'(A:|Answer:|Solution:|# Solution:|# Answer:|# Solution|# Answer|# Ans:|Ans:|\nAnswer:|\nAns:|\nSolution:|\n# Ans:|\n# Answer:|\n# Solution:|\n# Answer)'
    ])]
    qa = []
    q_regexes = [re.compile(p, re.DOTALL) for p in q_patterns]
    a_regexes = [re.compile(p, re.DOTALL) for p in a_patterns]
    q_starts = []
    for regex in q_regexes:
        q_starts.extend(list(regex.finditer(text)))
    q_starts = sorted(q_starts, key=lambda m: m.start())
    if not q_starts:
        manual_qs = list(re.finditer(r'(Q\d+\)|Q\d+\.|Q\d+|Question \d+|\d+\)|\d+\.|# .+)', text))
        q_starts = manual_qs
    for idx, q_match in enumerate(q_starts):
        q_start = q_match.end()
        q_end = q_starts[idx+1].start() if idx+1 < len(q_starts) else len(text)
        block = text[q_start:q_end]
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
            alt_a_match = re.search(r'(# Solution:|# Answer:|A:|Answer:|Solution:)', block)
            if alt_a_match:
                a_start = alt_a_match.end()
                answer = block[a_start:].strip()
                question = q_match.group(0) + block[:alt_a_match.start()].strip()
            else:
                answer = ''
                question = q_match.group(0) + block.strip()

        # Asset linking: find all asset placeholders in question/answer
        def find_asset_links(text, block_maps):
            table_tags = re.findall(r'\[\[TABLE:T(\d+)\]\]', text)
            img_tags = re.findall(r'\[\[IMG:I(\d+)\]\]', text)
            formula_tags = re.findall(r'\[\[FORMULA:F(\d+)\]\]', text)
            code_tags = re.findall(r'\[\[CODE:C(\d+)\]\]', text)
            caption_tags = re.findall(r'\[\[CAPTION:K(\d+)\]\]', text)
            # Link by index (T1, T2, ...) for tables, not full HTML
            tables = [f'T{i}' for i in table_tags]
            images = [f'I{i}' for i in img_tags]
            formulas = [f'F{i}' for i in formula_tags]
            codes = [f'C{i}' for i in code_tags]
            captions = [f'K{i}' for i in caption_tags]
            return {'tables': tables, 'images': images, 'formulas': formulas, 'codes': codes, 'captions': captions}

        asset_links = find_asset_links(question + answer, block_maps)
        evidence = []
        for tag, items in asset_links.items():
            for item in items:
                evidence.append({'type': tag, 'content': item})
        qa.append({
            'question': question.strip(),
            'answer': answer,
            'linked_tables': asset_links['tables'],
            'linked_images': asset_links['images'],
            'linked_formulas': asset_links['formulas'],
            'linked_codes': asset_links['codes'],
            'linked_captions': asset_links['captions'],
            'evidence': evidence
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

    # Load secrets from .streamlit/secrets.toml (st.secrets) if available, else fallback to .env/env
    token = None
    gemini_api_key = None
    if hasattr(st, "secrets") and "mineru" in st.secrets:
        token = st.secrets["mineru"]
    if hasattr(st, "secrets") and "GEMINI_API_KEY" in st.secrets:
        gemini_api_key = st.secrets["GEMINI_API_KEY"]
    if not token or not gemini_api_key:
        load_dotenv()
        token = token or os.getenv("mineru")
        gemini_api_key = gemini_api_key or os.getenv("GEMINI_API_KEY")
    if not token:
        st.error("MinerU API token not found in secrets.toml or .env.")
        st.stop()
    if not gemini_api_key:
        st.error("Gemini API key not found in secrets.toml or .env.")
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
    print(f"[DEBUG] block_maps before final_refined: {block_maps}")
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
    print(f"[DEBUG] final_refined before JSON dump: {final_refined}")

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