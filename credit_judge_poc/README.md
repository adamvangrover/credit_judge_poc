# Credit Judge PoC

Project overview, setup instructions, and usage guidelines for the Credit Judge Proof of Concept.

## Key Features & Structure

This Proof of Concept (PoC) is designed to demonstrate an LLM-based system for evaluating credit reports. It includes:

-   **Comprehensive Prompt Library (`src/prompts/judge_prompts.py`):**
    -   `CORPORATE_CREDIT_RATING_REPORT_TEMPLATE`: For generating detailed, structured AI credit analysis reports (JSON output).
    -   `SIMULATED_INPUT_REPORT_TEMPLATE`: For generating RAG-style text snippets (simulated retrieved context) for a company.
    -   `EXPERT_REVIEW_TABLE_GENERATION_TEMPLATE`: For generating expert human-style review tables (JSON output) of an existing credit report.
    -   `COMPARISON_TABLE_GENERATION_TEMPLATE`: For generating detailed Markdown comparison tables between an AI report and an expert report.

-   **Prompting Notebooks:**
    -   `notebooks/01_data_preparation.ipynb`: (Content to be developed) For exploring and preparing input data.
    -   `notebooks/02_judge_llm_prompting.ipynb`: Demonstrates how to assemble and use all prompts in the library, including conceptual LLM calls.
    -   `notebooks/03_data_generation_playground.ipynb`: A workspace to easily generate varied mock data (simulated inputs, AI reports, expert reviews, comparison tables) using the prompt library. Facilitates dataset augmentation.

-   **Mock Data:**
    -   AI-generated report examples (`data/reports_to_be_judged/`) simulating both structured JSON outputs and text-based RAG outputs.
    -   Gold standard review tables (`data/gold_standard_reviews/`) providing expert human assessments for comparison.
    -   Generated mock data can be stored in `data/generated_mock_data/`.

-   **Evaluation Scripts:** Python scripts (`evaluation_poc/evaluate_judge_outputs.py`) to compare AI-generated reports against gold standards.

-   **Core Logic (Conceptual & MVP):** Python modules for configuration, report parsing (`src/processing/report_parser.py`), review formatting (`src/processing/review_formatter.py`), and MVP orchestration (`run_credit_judge_poc.py`).

## Key Enhancements (Recent Updates)

The PoC has been enhanced with:
-   **Sophisticated Prompt Engineering & Library:** Implementation of a comprehensive library of detailed prompt templates for generating various types of credit-related content (AI reports, simulated inputs, expert reviews, comparison tables).
-   **Advanced Mock Data & Generation Tools:** Creation of more realistic mock data and a dedicated Jupyter notebook (`03_data_generation_playground.ipynb`) for generating further varied data samples.
-   **Enhanced Evaluation Framework:** The evaluation script outlines concepts for advanced evaluation.
-   **Guided Prompt Development:** The `02_judge_llm_prompting.ipynb` notebook updated to cover usage of all prompts in the library.
-   **MVP End-to-End Flow:** Implementation of a runnable `run_credit_judge_poc.py` script that simulates an end-to-end process using mock data.

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
    - A section-by-section comparison.
    - A qualitative summary extracted and formatted from the AI report.
    - A completion message.

This MVP run validates that the core components are connected and data can flow through the system.

### Using Notebooks

-   **`notebooks/01_data_preparation.ipynb`:** (Content to be developed) For exploring, preparing, and preprocessing input reports and expert review data.
-   **`notebooks/02_judge_llm_prompting.ipynb`:** Provides a detailed guide on how to use each prompt template from the `src/prompts/judge_prompts.py` library. It shows how to format the prompts with input data and includes conceptual examples of making LLM calls and handling their responses. This is a good starting point for experimenting with prompt variations.
-   **`notebooks/03_data_generation_playground.ipynb`:** A dedicated workspace for generating larger sets of mock data. Users can modify example scenarios and use the provided helper functions (which include conceptual LLM calls) to create:
    - Simulated RAG-style input reports.
    - Full AI-generated credit reports (JSON).
    - Expert review tables of existing reports (JSON).
    - Comparison tables between two reports (Markdown).
    The generated data can be saved to `data/generated_mock_data/` and used to expand the test dataset for the PoC.

```
