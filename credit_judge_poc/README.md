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
- **Core Logic (Conceptual):** Python modules for configuration, LLM interfacing, report parsing, review formatting, and core evaluation orchestration (under `src/`).

## Key Enhancements (Recent Updates)

The PoC has been enhanced with:
- **Sophisticated Prompt Engineering:** Implementation of a detailed prompt template for generating in-depth corporate credit rating reports, including sections for financial overrides, human example comparisons, and specific focus areas.
- **Advanced Mock Data:** Creation of more realistic and detailed mock data for both AI-generated reports (simulated RAG and structured JSON) and expert human review tables. This provides richer material for testing and evaluation.
- **Enhanced Evaluation Framework:** The evaluation script now includes logic to parse detailed JSON reports and reviews, perform basic quantitative score comparisons, and outlines concepts for future enhancements like semantic text comparison and probability-based scoring.
- **Guided Prompt Development:** The LLM prompting notebook (`notebooks/02_judge_llm_prompting.ipynb`) has been updated to reflect the usage of the new detailed prompt and includes placeholders for integrating more complex credit analysis techniques.

## Setup Instructions

(To be added - e.g., Python version, pip install requirements.txt)

## Usage Guidelines

(To be added - e.g., How to run the main script, how to use the notebooks)

