"""
parser/extractor.py
Segments document into Q/A blocks using RuleSet, restores atomic blocks, tracks evidence.
"""

import json
import re

def parse_document(normalized_md_path, ruleset_path, block_maps_path, output_dir):
    with open(normalized_md_path, "r", encoding="utf-8") as f:
        md = f.read()
    with open(ruleset_path, "r", encoding="utf-8") as f:
        ruleset = json.load(f)
    with open(block_maps_path, "r", encoding="utf-8") as f:
        block_maps = json.load(f)
    # Load tables if present
    import os
    tables_path = os.path.join(output_dir, "tables.json")
    tables = []
    if os.path.exists(tables_path):
        with open(tables_path, "r", encoding="utf-8") as tf:
            tables = json.load(tf)
    # Compile all patterns from Gemini-mined ruleset
    q_patterns = [re.compile(p, re.IGNORECASE) for p in ruleset["question_start_patterns"]]
    a_patterns = [re.compile(p, re.IGNORECASE) for p in ruleset["answer_start_patterns"]]
    stop_patterns = [re.compile(p, re.IGNORECASE) for p in ruleset["stop_conditions"]]
    items = []
    lines = md.splitlines()
    n = len(lines)
    i = 0
    while i < n:
        matched = None
        for qp in q_patterns:
            if qp.match(lines[i]):
                matched = qp.pattern
                break
        is_numbered_question = re.match(r"^\d+[\)\.][^\w]*.+", lines[i].strip())
        lookahead_solution = False
        lookahead_idx = i + 1
        if not matched and is_numbered_question:
            for j in range(lookahead_idx, min(lookahead_idx + 5, n)):
                if re.match(r"^(##\s*)?Solution:?", lines[j].strip(), re.IGNORECASE):
                    lookahead_solution = True
                    break
        if matched or lookahead_solution:
            q_start = i
            q_text = lines[i]
            answer_lines = []
            found_answer = False
            answer_tables = set()
            j = i + 1
            while j < n:
                line = lines[j].strip()
                if re.match(r"^(##\s*)?Solution:?", line, re.IGNORECASE):
                    found_answer = True
                    j += 1
                    while j < n:
                        next_line = lines[j].strip()
                        if any(qp.match(next_line) for qp in q_patterns) or re.match(r"^#+\s*.*", next_line) or re.match(r"^\d+[\)\.][^\w]*.+", next_line):
                            break
                        # Detect table references
                        table_match = re.match(r"\[\[(TABLE_BLOCK:[^\]]+)\]\]", lines[j])
                        if table_match:
                            answer_tables.add(table_match.group(1).replace("BLOCK:", ":"))
                        answer_lines.append(lines[j])
                        j += 1
                    break
                j += 1
            answer_text = "\n".join(answer_lines).strip() if found_answer else ""
            # Restore atomic blocks (except tables, which are referenced)
            for block_id in block_maps:
                if block_id.startswith("TABLE_BLOCK:"):
                    continue
                answer_text = answer_text.replace(f"[[{block_id}]]", block_maps[block_id])
            items.append({
                "id": f"Q{len(items)+1:03d}",
                "question": {"text": q_text},
                "answer": {
                    "text_markdown": answer_text,
                    "tables": sorted(list(answer_tables)) if answer_tables else []
                },
                "evidence": {"source_span": [q_start, j], "matched_pattern": matched if matched else "numbered+solution"}
            })
            i = j
        else:
            i += 1
    # Save extracted items
    with open(f"{output_dir}/extracted_items.json", "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)
    return items
