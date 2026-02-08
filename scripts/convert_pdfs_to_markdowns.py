"""
Batch convert all PDFs in pdfs/ to markdowns/ using MinerU (magic-pdf).
Extracts images and saves them alongside markdown.
"""
import os
from magic_pdf import MagicPDF

PDF_DIR = "pdfs"
MARKDOWN_DIR = "markdowns"
os.makedirs(MARKDOWN_DIR, exist_ok=True)

for pdf_file in os.listdir(PDF_DIR):
    if not pdf_file.lower().endswith(".pdf"):
        continue
    pdf_path = os.path.join(PDF_DIR, pdf_file)
    base_name = os.path.splitext(pdf_file)[0]
    output_dir = os.path.join(MARKDOWN_DIR, base_name)
    os.makedirs(output_dir, exist_ok=True)
    parser = MagicPDF(pdf_path)
    # Save as markdown (with images extracted)
    result = parser.parse(output_dir=output_dir, output_format="markdown")
    # Move markdown to markdowns/ root for pipeline compatibility
    md_path = os.path.join(output_dir, f"{base_name}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(result.markdown)
    print(f"Converted {pdf_file} -> {md_path}")
