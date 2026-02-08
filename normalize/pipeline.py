"""
normalize/pipeline.py
Extracts and replaces atomic blocks, normalizes whitespace, de-hyphenates, injects page anchors.
"""

import re
import os

def normalize_markdown(md_path, output_dir):
    with open(md_path, "r", encoding="utf-8") as f:
        md = f.read()
    block_maps = {}
    import json
    # Improved table extraction: robustly find all markdown tables
    table_objs = []
    table_blocks = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        # Detect start of a markdown table (header row with |, then separator row with ---)
        if '|' in lines[i] and i+1 < len(lines) and re.match(r"^\s*\|?\s*:?[- ]+:?\s*(\|\s*:?[- ]+:?\s*)+\|?\s*$", lines[i+1]):
            table_start = i
            table_end = i+2
            # Find end of table (next non-table line)
            while table_end < len(lines) and ('|' in lines[table_end] and not lines[table_end].strip().startswith('#')):
                table_end += 1
            table_md = '\n'.join(lines[table_start:table_end]) + '\n'
            block_id = f"TABLE_BLOCK:{len(table_objs)+1}"
            table_blocks.append((table_start, table_end, block_id, table_md))
            # Parse table to grid
            table_lines = [l for l in table_md.splitlines() if l.strip()]
            if len(table_lines) >= 2:
                headers = [h.strip() for h in table_lines[0].strip('|').split('|')]
                rows = []
                for row_line in table_lines[2:]:
                    row = [c.strip() for c in row_line.strip('|').split('|')]
                    if len(row) == len(headers):
                        rows.append(row)
                table_objs.append({
                    "id": block_id.replace("BLOCK:", ":"),
                    "source": {"format": "markdown", "content": table_md},
                    "grid": {"headers": headers, "rows": rows},
                    "notes": {"merged_cells": False, "confidence": 1.0}
                })
            i = table_end
        else:
            i += 1
    # Replace tables in markdown with block IDs
    for table_start, table_end, block_id, table_md in reversed(table_blocks):
        md_lines = md.splitlines()
        md_lines = md_lines[:table_start] + [f"[[{block_id}]]"] + md_lines[table_end:]
        md = '\n'.join(md_lines)
        block_maps[block_id] = table_md
    # Save tables array
    with open(os.path.join(output_dir, "tables.json"), "w", encoding="utf-8") as f:
        json.dump(table_objs, f, indent=2)
    # Replace code fences
    code_pattern = re.compile(r"```[\w\W]+?```", re.MULTILINE)
    codes = code_pattern.findall(md)
    for i, code in enumerate(codes):
        block_id = f"CODE_BLOCK:{i+1}"
        md = md.replace(code, f"[[{block_id}]]")
        block_maps[block_id] = code
    # Replace images
    img_pattern = re.compile(r"!\[.*?\]\((.*?)\)")
    imgs = img_pattern.findall(md)
    for i, img in enumerate(imgs):
        block_id = f"IMG:{i+1}"
        md = md.replace(img, f"[[{block_id}]]")
        block_maps[block_id] = img
    # Normalize whitespace, de-hyphenate, but preserve line breaks for headings, numbered questions, and Solution blocks
    # Insert newlines before headings, numbered questions (1. or 1)), and 'Solution:'
    md = re.sub(r"(#+\s*.*)", r"\n\1", md)
    md = re.sub(r"(\n)?(\d+[\)\.] )", r"\n\2", md)
    md = re.sub(r"(\n)?(Q\d+\. )", r"\n\2", md)
    md = re.sub(r"(\n)?(Question \d+\. )", r"\n\2", md)
    md = re.sub(r"(\n)?(Solution:?|## Solution:?|\*\*Solution:?\*\*)", r"\n\2", md, flags=re.IGNORECASE)
    # Now collapse multiple spaces but preserve newlines
    md = re.sub(r"[ \t]+", " ", md)
    md = re.sub(r"-\s+", "", md)
    md = re.sub(r"\n+", "\n", md)
    # Save normalized.md and block_maps.json
    with open(os.path.join(output_dir, "normalized.md"), "w", encoding="utf-8") as f:
        f.write(md)
    with open(os.path.join(output_dir, "block_maps.json"), "w", encoding="utf-8") as f:
        import json
        json.dump(block_maps, f, indent=2)
    return md, block_maps
