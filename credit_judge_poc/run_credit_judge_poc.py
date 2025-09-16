# Main script to execute the Credit Judge PoC pipeline.
# Loads a report, processes it, and evaluates it against a gold standard.

import os
import json

# Assuming src is in PYTHONPATH or script is run from project root.
from credit_judge_poc.src.processing.report_parser import load_ai_report_from_json
from credit_judge_poc.src.processing.review_formatter import format_ai_output_for_review
from credit_judge_poc.evaluation_poc.evaluate_judge_outputs import (
    load_json_file as load_gold_standard, # Renaming for clarity
    display_qualitative_comparison
)

def main():
    """
    Main function to run the Credit Judge PoC MVP pipeline.
    """
    print("Starting Credit Judge PoC - MVP Run...")

    # --- 1. Define File Paths ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = script_dir if os.path.basename(script_dir) == "credit_judge_poc" else os.path.dirname(script_dir)

    ai_report_filename = "dkng_ai_report.json"
    gold_standard_filename = "dkng_review_table.json"

    ai_report_path = os.path.join(base_path, "data", "reports_to_be_judged", ai_report_filename)
    gold_standard_path = os.path.join(base_path, "data", "gold_standard_reviews", gold_standard_filename)
    
    print(f"\n- AI Report Path: {ai_report_path}")
    print(f"- Gold Standard Path: {gold_standard_path}")

    # --- 2. Load AI Report (Simulated LLM Output) ---
    print("\n--- Loading Simulated AI Report ---")
    ai_report_data = load_ai_report_from_json(ai_report_path)
    if not ai_report_data:
        print("Failed to load AI report. Exiting.")
        return
    print(f"Successfully loaded AI report: {ai_report_filename}")

    # --- 3. Load Gold Standard Review ---
    print("\n--- Loading Gold Standard Review ---")
    gold_standard_data = load_gold_standard(gold_standard_path)
    if not gold_standard_data:
        print("Failed to load Gold Standard review. Exiting.")
        return
    print(f"Successfully loaded Gold Standard review: {gold_standard_filename}")

    # --- 4. (Optional) Format AI Output for a Quick Summary ---
    # This step demonstrates the formatter, though the detailed evaluation
    # now uses the raw AI report data for a fuller comparison.
    print("\n--- Formatting AI Output for Quick Summary (for context) ---")
    formatted_ai_output = format_ai_output_for_review(ai_report_data)
    if formatted_ai_output:
        print(f"Company: {formatted_ai_output.get('companyName')}")
        print(f"Inferred Rating by AI: {formatted_ai_output.get('inferredRating')} {formatted_ai_output.get('outlook')}")
    else:
        print("Could not format AI output for summary.")


    # --- 5. Evaluate AI Output against Gold Standard ---
    # This now calls the enhanced function to show a rich, qualitative comparison.
    display_qualitative_comparison(ai_report_data, gold_standard_data)

    print("\nCredit Judge PoC - MVP Run Completed.")

if __name__ == "__main__":
    main()
