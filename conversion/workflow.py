"""
conversion/workflow.py
Handles PDF → Markdown conversion using Datalab SDK workflow steps.
"""

import os
from datalab_sdk import DatalabClient, WorkflowStep, InputConfig


def get_client():
    DATALAB_API_KEY = os.getenv("DATALAB_API_KEY")
    if not DATALAB_API_KEY:
        raise EnvironmentError("DATALAB_API_KEY not found in environment.")
    return DatalabClient(api_key=DATALAB_API_KEY)

def convert_pdf_simple(pdf_path, output_dir):
    """Simple mode: direct PDF to Markdown conversion."""
    client = get_client()
    result = client.convert(pdf_path, output_format="markdown", use_llm=False)
    # Save markdown and assets
    with open(os.path.join(output_dir, "document.md"), "w", encoding="utf-8") as f:
        f.write(result.markdown)
    # Save images/assets if present
    # ...existing code...
    return result

def convert_pdf_workflow(pdf_path, output_dir, settings=None):
    """Workflow mode: uses marker_parse, await_parse_quality, conditional steps."""
    client = get_client()
    steps = [
        WorkflowStep(
            step_type="marker_parse",
            input_config=InputConfig(
                file_path=pdf_path,
                use_llm=False,
                output_format="markdown",
                **(settings or {})
            )
        ),
        WorkflowStep(step_type="await_parse_quality"),
        WorkflowStep(step_type="conditional")
    ]
    workflow = client.create_workflow(steps)
    result = client.run_workflow(workflow)
    # Save markdown, assets, and metadata
    with open(os.path.join(output_dir, "document.md"), "w", encoding="utf-8") as f:
        f.write(result.markdown)
    # Save conversion metadata
    with open(os.path.join(output_dir, "conversion_metadata.json"), "w", encoding="utf-8") as f:
        f.write(result.metadata_json)
    # Save images/assets if present
    # ...existing code...
    return result

def sanity_check_step_types():
    """Sanity check: verify workflow step keys exist."""
    client = get_client()
    step_types = client.get_step_types()
    required = ["marker_parse", "await_parse_quality", "conditional", "marker_segment"]
    for key in required:
        if key not in step_types:
            raise ValueError(f"Missing required step type: {key}")
    return True
