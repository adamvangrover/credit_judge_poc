# Credit Judge PoC

Project overview, setup instructions, and usage guidelines for the Credit Judge Proof of Concept.

## Key Features & Structure

This Proof of Concept (PoC) is designed to demonstrate an LLM-based system for evaluating credit reports. It includes:

-   **Comprehensive Prompt Library (`src/prompts/judge_prompts.py`):** A suite of templates for generating AI reports, simulated inputs, expert reviews, and comparison tables.
-   **Rich Mock Data:** Realistic examples of AI-generated reports and gold standard human reviews.
-   **End-to-End MVP Script (`run_credit_judge_poc.py`):** A runnable script demonstrating the core workflow: loading data, formatting it, and running an evaluation.
-   **Enhanced Evaluation Script (`evaluation_poc/evaluate_judge_outputs.py`):** Provides a rich, side-by-side qualitative comparison between the AI-generated report and the gold standard review.
-   **Jupyter Notebooks:** Workspaces for data preparation (`01_...`), prompt experimentation (`02_...`), and mock data generation (`03_...`).
-   **Modular Codebase (`src/`):** Organized Python modules for processing, LLM interaction (conceptual), and core logic.

## Setup Instructions

1.  **Python Version:** Python 3.9+ is recommended.
2.  **Dependencies:** For the current MVP, no external packages are required. The project uses standard Python libraries like `json`, `os`, and `textwrap`.
3.  **Future Dependencies:** If the project is extended to use external libraries (e.g., an LLM SDK), they will be listed in the `requirements.txt` file. You would install them using:
    ```bash
    pip install -r credit_judge_poc/requirements.txt
    ```

## Usage Guidelines

### 1. Running the End-to-End MVP

The main script simulates the entire process using mock data.

1.  **Navigate to Project Root:** Open your terminal and change to the directory containing the `credit_judge_poc` folder.
2.  **Run the Script:** Execute the main MVP script:
    ```bash
    python credit_judge_poc/run_credit_judge_poc.py
    ```
3.  **Expected Output:**
    The script will print a detailed, section-by-section qualitative comparison to the console. For each section of the credit report, you will see:
    - The **Gold Standard Review**, including the human expert's score and qualitative feedback.
    - The **Corresponding AI Report Content**, showing the raw text, list, or JSON that the AI generated for that section.
    This provides a clear, side-by-side view for evaluating the AI's performance.

### 2. Running the Evaluation Script Directly

The evaluation script can also be run as a standalone utility to just view the comparison.

-   **Run from the project root:**
    ```bash
    python credit_judge_poc/evaluation_poc/evaluate_judge_outputs.py
    ```
    This will produce the same detailed qualitative comparison report as the main MVP script.

### 3. Using the Notebooks

-   **`notebooks/01_data_preparation.ipynb`:** (Content to be developed) For exploring and preparing input data.
-   **`notebooks/02_judge_llm_prompting.ipynb`:** A guide to using the prompt library. It shows how to format prompts and provides conceptual examples of LLM calls.
-   **`notebooks/03_data_generation_playground.ipynb`:** A workspace for generating new mock data (AI reports, expert reviews, etc.) to expand the test set.
