"""
cli.py
Main CLI entry point for PDF Q/A extraction pipeline.
"""

import argparse
import os
from conversion.workflow import convert_pdf_workflow, convert_pdf_simple, sanity_check_step_types
from normalize.pipeline import normalize_markdown
from pattern_mining.mining import mine_patterns
from parser.extractor import parse_document
from validation.checks import validate_extraction


def main():
    parser = argparse.ArgumentParser(description="PDF Q/A Extraction Pipeline")
    parser.add_argument("extract", nargs=1, help="PDF file path")
    parser.add_argument("--out", required=True, help="Output JSON file")
    parser.add_argument("--mode", choices=["simple", "workflow"], default="workflow")
    parser.add_argument("--max-pages", type=int)
    parser.add_argument("--force-ocr", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    pdf_path = args.extract[0]
    output_dir = os.path.dirname(args.out)
    os.makedirs(output_dir, exist_ok=True)

    sanity_check_step_types()

    settings = {}
    if args.max_pages:
        settings["max_pages"] = args.max_pages
    if args.force_ocr:
        settings["force_ocr"] = True

    if args.mode == "simple":
        conversion_result = convert_pdf_simple(pdf_path, output_dir)
    else:
        conversion_result = convert_pdf_workflow(pdf_path, output_dir, settings)

    normalized_md, block_maps = normalize_markdown(os.path.join(output_dir, "document.md"), output_dir)
    ruleset = mine_patterns(os.path.join(output_dir, "normalized.md"), output_dir)
    items = parse_document(os.path.join(output_dir, "normalized.md"), os.path.join(output_dir, "ruleset.json"), os.path.join(output_dir, "block_maps.json"), output_dir)
    warnings, stats = validate_extraction(os.path.join(output_dir, "extracted_items.json"), os.path.join(output_dir, "ruleset.json"), os.path.join(output_dir, "conversion_metadata.json"))

    final_json = {
        "document": {
            "doc_id": conversion_result.get("doc_id"),
            "file_name": os.path.basename(pdf_path),
            "sha256": conversion_result.get("sha256"),
            "page_count": conversion_result.get("page_count"),
            "conversion": conversion_result.get("engine", {}),
        },
        "ruleset": ruleset,
        "items": items,
        "warnings": warnings,
        "stats": stats
    }
    with open(args.out, "w", encoding="utf-8") as f:
        import json
        json.dump(final_json, f, indent=2)

    print(f"Parse quality: {stats.get('parse_quality')}")
    print(f"Questions found: {stats.get('questions_found')}")
    print(f"Confidence: {stats.get('pattern_confidence')}")
    if warnings:
        print("Warnings:", warnings)
    if args.debug:
        print("Top candidate question markers:", ruleset.get("question_start_patterns"))
        print("Chosen regex family:", ruleset.get("diagnostics", {}).get("families"))

if __name__ == "__main__":
    main()
