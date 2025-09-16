import os
import sys
from evaluation.evaluator import display_qualitative_comparison, load_json_file
from src.llm_interface.llm_handler import generate_report
from src.prompts.prompts import get_report_generation_prompt

def main():
    """
    Main function to run the Credit Judge v2 pipeline.
    """
    print("Starting Credit Judge v2 Run...")

    # --- 1. Generate AI Report via Simulated LLM Call ---
    print("\n--- Generating AI Credit Report ---")
    company_name = "DraftKings Inc."
    ticker_symbol = "DKNG"

    # Get the prompt
    prompt = get_report_generation_prompt(company_name, ticker_symbol)

    # "Call" the LLM to get the report
    # In this version, this is a simulated call.
    ai_report_data = generate_report(prompt)
    if not ai_report_data:
        print("\nFailed to generate AI report. Exiting.")
        return
    print(f"--- Successfully generated AI report for {company_name} ---")


    # --- 2. Load Gold Standard Review ---
    print("\n--- Loading Gold Standard Review for Comparison ---")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gold_standard_path = os.path.join(script_dir, "data", "gold_standard.json")

    gold_standard_data = load_json_file(gold_standard_path)
    if not gold_standard_data:
        print("\nFailed to load Gold Standard review. Exiting.")
        return
    print(f"Successfully loaded Gold Standard review from: {gold_standard_path}")


    # --- 3. Evaluate and Display Comparison ---
    # This calls the function to show a rich, qualitative comparison.
    display_qualitative_comparison(ai_report_data, gold_standard_data)

    print("\nCredit Judge v2 Run Completed.")

if __name__ == "__main__":
    # Add the v2 directory to the Python path to allow for package-like imports
    project_root = os.path.dirname(os.path.abspath(__file__))
    # Go one level up to add the parent of credit_judge_v2 to the path
    sys.path.insert(0, os.path.dirname(project_root))
    main()
