# Credit Judge PoC

Project overview, setup instructions, and usage guidelines for the Credit Judge Proof of Concept.

## Key Features & Structure

This Proof of Concept (PoC) is designed to demonstrate an LLM-based system for evaluating credit reports. It includes:
- **Detailed Prompting:** Sophisticated prompt templates (see `src/prompts/judge_prompts.py`) for generating comprehensive corporate credit rating reports.
- **Prompting Notebook:** A Jupyter notebook (`notebooks/02_judge_llm_prompting.ipynb`) that demonstrates how to assemble and use these prompts, including conceptual placeholders for advanced analytical logic.
- **Mock Data:**
    - AI-generated report examples (`data/reports_to_be_judged/`) simulating both structured JSON outputs and text-based RAG outputs.
    - Gold standard review tables (`data/gold_standard_reviews/`) providing expert human assessments for comparison.
- **Evaluation Scripts:** Python scripts (`evaluation_poc/evaluate_judge_outputs.py`) to compare AI-generated reports against gold standards, including basic score comparisons and conceptual placeholders for more advanced NLP-based evaluations and probability mapping.
- **Core Logic (Conceptual & MVP):** Python modules for configuration, report parsing (`src/processing/report_parser.py`), review formatting (`src/processing/review_formatter.py`), and MVP orchestration (`run_credit_judge_poc.py`).

## Key Enhancements (Recent Updates)

The PoC has been enhanced with:
- **Sophisticated Prompt Engineering:** Implementation of a detailed prompt template for generating in-depth corporate credit rating reports.
- **Advanced Mock Data:** Creation of more realistic and detailed mock data for both AI-generated reports and expert human review tables.
- **Enhanced Evaluation Framework:** The evaluation script now includes logic to parse detailed JSON reports/reviews and outlines concepts for advanced evaluation.
- **Guided Prompt Development:** The LLM prompting notebook reflects the usage of the new detailed prompt.
- **MVP End-to-End Flow:** Implementation of a runnable `run_credit_judge_poc.py` script that simulates an end-to-end process using mock data.

## Setup Instructions

1.  **Python Version:** Python 3.9+ is recommended.
2.  **Dependencies:** Currently, the MVP relies on standard Python libraries (json, os). If specific packages were added (e.g., for a real LLM SDK), they would be listed in `requirements.txt`.
    ```bash
    # (Example if requirements.txt existed and was populated)
    # pip install -r requirements.txt
    ```
    For the current MVP, no external packages beyond standard Python are strictly necessary to run `run_credit_judge_poc.py`.

## Usage Guidelines

### MVP Usage Instructions

The Minimum Viable Process (MVP) demonstrates the basic end-to-end flow of the system using mock data.

1.  **Navigate to Project Root:** Open your terminal and change directory to the root of the `credit_judge_poc` project.
2.  **Run the Script:** Execute the main MVP script using Python:
    ```bash
    python credit_judge_poc/run_credit_judge_poc.py
    ```
    (If `credit_judge_poc` is directly in your PYTHONPATH, you might also run it as `python -m credit_judge_poc.run_credit_judge_poc`)

3.  **Expected Output:**
    The script will print to the console:
    - Confirmation of files being loaded (mock AI report and gold standard review).
    - A note about the "Overall Score" being from the gold standard's perspective.
    - A section-by-section comparison. For the MVP, since the mock AI report (`dkng_ai_report.json`) doesn't contain self-assigned quantitative scores for its sections that directly map to the gold standard's review scores, you will likely see "AI Score: Not Found/Not Applicable" for many quantitative comparisons within `evaluate_report_sections`. This is expected. The primary purpose is to show the flow and structure.
    - A qualitative summary extracted and formatted from the AI report (e.g., company name, inferred rating, key strengths/weaknesses summary).
    - A completion message.

This MVP run validates that the core components are connected and data can flow through the system. Future iterations will involve replacing mock components with live LLM calls and more sophisticated processing.

### Using Notebooks

-   **`notebooks/01_data_preparation.ipynb`:** (Content to be developed) For exploring and preparing input data.
-   **`notebooks/02_judge_llm_prompting.ipynb`:** Demonstrates how to assemble the detailed prompt for generating a corporate credit rating report. This can be used as a starting point for experimenting with different prompt parameters or sending prompts to an LLM.

```
