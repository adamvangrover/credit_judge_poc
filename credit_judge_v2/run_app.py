import os
import sys

# Add the parent directory to sys.path to ensure modules can be found
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from credit_judge_v2.evaluation.evaluator import display_qualitative_comparison, load_json_file
from credit_judge_v2.src.llm_interface.llm_handler import generate_report
from credit_judge_v2.src.prompts.prompts import get_report_generation_prompt
from credit_judge_v2.src.processing.analysis import analyze_report_content
from credit_judge_v2.src.utils.html_generator import generate_html_report

def main():
    """
    Main function to run the Credit Judge v2 pipeline.
    """
    print("Starting Credit Judge v2 Run...")

    # --- 0. User Selection ---
    print("\nSelect a Company for Analysis:")
    print("1. DraftKings Inc. (DKNG)")
    print("2. Tesla Inc. (TSLA)")

    choice = input("Enter choice (1 or 2): ").strip()

    if choice == "2":
        company_name = "Tesla Inc."
        ticker_symbol = "TSLA"
        gold_standard_file = "tesla.json"
    else:
        company_name = "DraftKings Inc."
        ticker_symbol = "DKNG"
        gold_standard_file = "draftkings.json"

    # --- 1. Generate AI Report via Simulated LLM Call ---
    print(f"\n--- Generating AI Credit Report for {company_name} ---")

    # Get the prompt
    prompt = get_report_generation_prompt(company_name, ticker_symbol)

    # "Call" the LLM to get the report
    ai_report_data = generate_report(prompt, company_name, ticker_symbol)
    if not ai_report_data:
        print("\nFailed to generate AI report. Exiting.")
        return
    print(f"--- Successfully generated AI report for {company_name} ---")


    # --- 2. Load Gold Standard Review ---
    print("\n--- Loading Gold Standard Review for Comparison ---")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    gold_standard_path = os.path.join(script_dir, "data", "gold_standards", gold_standard_file)

    gold_standard_data = load_json_file(gold_standard_path)
    if not gold_standard_data:
        print("\nFailed to load Gold Standard review. Exiting.")
        return
    print(f"Successfully loaded Gold Standard review from: {gold_standard_path}")


    # --- 3. Evaluate and Display Comparison ---
    # This calls the function to show a rich, qualitative comparison on console.
    display_qualitative_comparison(ai_report_data, gold_standard_data)

    # --- 4. Generate HTML Report ---
    print("\n--- Generating HTML Report ---")

    # Perform quantitative analysis for the HTML report
    analysis_results = analyze_report_content(ai_report_data)

    # Generate the file
    output_filename = f"report_{ticker_symbol}.html"
    output_path = os.path.join(script_dir, "output", output_filename)
    generate_html_report(ai_report_data, analysis_results, gold_standard_data, output_path)

    print("\nCredit Judge v2 Run Completed.")

if __name__ == "__main__":
    main()
