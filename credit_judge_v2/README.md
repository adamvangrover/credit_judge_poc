# Credit Judge v2

This directory contains a self-contained, cleaned-up, and production-ready version of the Credit Judge PoC.

## Overview

This system demonstrates a dynamic, end-to-end process for generating an AI credit report and then evaluating it against a human-created "gold standard" review.

The key features of this version are:
- **Production-Ready LLM Interface:** The application is now capable of making real API calls to OpenAI's GPT models to generate the AI credit report.
- **Graceful Fallback:** If an OpenAI API key is not provided, the system will gracefully fall back to using a mock response, ensuring the application is always runnable.
- **Rich Qualitative Evaluation:** The system provides a detailed, side-by-side comparison of the AI-generated report and the gold standard review.
- **Secure Configuration:** API keys are managed securely using environment variables, with a `.env.example` file provided for guidance.

## Setup and Usage

### 1. Install Dependencies

First, install the necessary Python packages:

```bash
pip install -r credit_judge_v2/requirements.txt
```

### 2. Configure Your API Key (Optional)

To use a real LLM for report generation, you need to provide an OpenAI API key.

1.  **Create a `.env` file:** In the `credit_judge_v2` directory, make a copy of the `.env.example` file and name it `.env`.
    ```bash
    cp credit_judge_v2/.env.example credit_judge_v2/.env
    ```
2.  **Add your API key:** Open the new `.env` file and replace `"your_openai_api_key_here"` with your actual OpenAI API key.

### 3. Run the Application

The application can be run with a single command from the project's root directory:

```bash
python credit_judge_v2/run_app.py
```

-   **If you provided an API key**, the script will call the OpenAI API to generate a new credit report.
-   **If you did not provide an API key**, the script will display a warning and use a built-in mock report.

In both cases, it will then proceed to load the gold standard review and display a detailed, section-by-section comparison.
