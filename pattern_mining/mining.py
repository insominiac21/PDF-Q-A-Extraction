"""
pattern_mining/mining.py
Discovers question/answer patterns, clusters candidates, scores families, outputs ruleset.json.
"""

import re
import json
import os

def mine_patterns(normalized_md_path, output_dir):
    from dotenv import load_dotenv
    load_dotenv()
    with open(normalized_md_path, "r", encoding="utf-8") as f:
        lines = [l.rstrip() for l in f if l.strip()]
    # Sample: first 20, last 20, and 10 random lines for diversity
    import random
    sample_lines = lines[:20] + lines[-20:]
    if len(lines) > 60:
        sample_lines += random.sample(lines[20:-20], min(10, len(lines)-40))
    snippet = "\n".join(sample_lines)
    # Finetuned Gemini prompt for robust, generic Q/A regex mining
    prompt = (
        "You are an expert in educational document parsing. "
        "Given the following markdown, return a JSON object with two arrays: "
        "'question_patterns': robust regexes for question headers (including numbered, bulleted, bolded, and heading-based questions, e.g., '1)', 'Q1.', '## Question', etc.), and "
        "'answer_patterns': robust regexes for answer blocks. "
        "For answer_patterns, include patterns that match:\n"
        "- Explicit answer markers (e.g., 'Solution:', 'Answer:', 'Ans:', 'Explanation:')\n"
        "- Paragraphs, lists, equations, tables, or code blocks that immediately follow a question (even if not explicitly marked)\n"
        "- Multi-line answers, including those with LaTeX, code, or markdown tables\n"
        "- Any block that is likely to be an answer in educational markdowns, including implicit answers\n"
        "- Avoid overfitting to specific content; prefer generic, reusable patterns\n"
        "- Do NOT include any hardcoded question/answer text from the sample\n"
        "- Patterns should be compatible with Python's re module\n"
        "Return only the JSON object, no explanations.\n"
        "Markdown sample:\n" + snippet
    )
    gemini_response = None
    question_patterns = []
    answer_patterns = []
    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash-latest",
            contents=prompt
        )
        gemini_response = response.text
        import json as _json
        result = _json.loads(gemini_response)
        if isinstance(result, dict):
            question_patterns = result.get("question_patterns", [])
            answer_patterns = result.get("answer_patterns", [])
    except Exception:
        # fallback: use a minimal generic pattern
        question_patterns = [r"^#+\\s*.*", r"^\\d+[\\)\\.] .+"]
        answer_patterns = [r"^.+$"]
    # Stop conditions: generic
    stop_patterns = [r"^#+ \\d+\\. ", r"^\\d+\\. ", r"^(Q\\d+|Question \\d+|Problem|Exercise)", r"^SECTION", r"^PART", r"^#"]
    exclusions = [r"Figure", r"Table"]
    confidence = len(question_patterns) / 10 if question_patterns else 0
    ruleset = {
        "question_start_patterns": question_patterns,
        "answer_start_patterns": answer_patterns,
        "stop_conditions": stop_patterns,
        "exclusions": exclusions,
        "confidence": confidence,
        "diagnostics": {"gemini_response": gemini_response}
    }
    with open(f"{output_dir}/ruleset.json", "w", encoding="utf-8") as f:
        json.dump(ruleset, f, indent=2)
    return ruleset
