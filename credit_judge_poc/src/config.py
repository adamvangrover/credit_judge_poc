# Configuration settings for the application.
# e.g., API keys, model names, file paths, default parameters.

import os

# Get the absolute path of the project root directory.
# This assumes config.py is in credit_judge_poc/src/
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- File Paths ---
# Define paths to key data files.
# These can be overridden by command-line arguments or environment variables if needed.

# Default path for the AI-generated report to be judged (input)
DEFAULT_AI_REPORT_DIR = os.path.join(PROJECT_ROOT, "data", "reports_to_be_judged")
DEFAULT_AI_REPORT_FILENAME = "dkng_ai_report.json" # Example default
DEFAULT_AI_REPORT_PATH = os.path.join(DEFAULT_AI_REPORT_DIR, DEFAULT_AI_REPORT_FILENAME)

# Default path for the gold standard review table (for comparison)
DEFAULT_GOLD_STANDARD_DIR = os.path.join(PROJECT_ROOT, "data", "gold_standard_reviews")
DEFAULT_GOLD_STANDARD_FILENAME = "dkng_review_table.json" # Example default
DEFAULT_GOLD_STANDARD_PATH = os.path.join(DEFAULT_GOLD_STANDARD_DIR, DEFAULT_GOLD_STANDARD_FILENAME)

# Path to prompt templates
PROMPTS_DIR = os.path.join(PROJECT_ROOT, "src", "prompts")
JUDGE_PROMPTS_FILE = os.path.join(PROMPTS_DIR, "judge_prompts.py")


# --- LLM Configuration (Placeholders) ---
# These would be used if making live LLM calls.
LLM_API_KEY_ENV_VAR = "YOUR_LLM_API_KEY"  # Environment variable name for the API key
DEFAULT_LLM_MODEL_NAME = "your-preferred-model-name" # e.g., "gemini-1.5-flash-latest"

# --- Output Configuration ---
DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "output_reviews")


# Example of how to use these in other scripts:
# from credit_judge_poc.src.config import DEFAULT_AI_REPORT_PATH, DEFAULT_LLM_MODEL_NAME
#
# print(f"Default AI report path: {DEFAULT_AI_REPORT_PATH}")
# print(f"Default LLM Model: {DEFAULT_LLM_MODEL_NAME}")

# Ensure output directory exists (optional, can be handled by writing functions)
# if not os.path.exists(DEFAULT_OUTPUT_DIR):
#     try:
#         os.makedirs(DEFAULT_OUTPUT_DIR)
#         print(f"Created output directory: {DEFAULT_OUTPUT_DIR}")
#     except OSError as e:
#         print(f"Error creating output directory {DEFAULT_OUTPUT_DIR}: {e}")
