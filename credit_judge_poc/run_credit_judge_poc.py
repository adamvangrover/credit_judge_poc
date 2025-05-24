# Main script to execute the Credit Judge PoC pipeline.
# Loads a report, processes it section by section using the Credit Judge LLM,
# and outputs the structured evaluation.


import os
import json # For printing dicts nicely

# Assuming src is in PYTHONPATH or script is run from project root.
from credit_judge_poc.src.processing.report_parser import load_ai_report_from_json
from credit_judge_poc.src.processing.review_formatter import format_ai_output_for_review
from credit_judge_poc.evaluation_poc.evaluate_judge_outputs import (
    load_json_file as load_gold_standard, # Renaming for clarity
    compare_scores, 
    evaluate_report_sections
)
# In a full version, config might come from a dedicated config file or environment variables
# from credit_judge_poc.src.config import AI_REPORT_PATH, GOLD_STANDARD_REPORT_PATH

def main():
    """
    Main function to run the Credit Judge PoC MVP pipeline.
    """
    print("Starting Credit Judge PoC - MVP Run...")

    # --- 1. Define File Paths (MVP: hardcoded relative paths) ---
    # In a real app, these would come from config.py or arguments
    script_dir = os.path.dirname(os.path.abspath(__file__)) # More robust path finding
    if os.path.basename(script_dir) == "credit_judge_poc": # Running from project root
        base_path = script_dir
    else: # Assuming script is in credit_judge_poc directory itself
        base_path = os.path.dirname(script_dir)


    # Default paths for MVP
    # These paths assume the script is run from the root of the 'credit_judge_poc' directory,
    # OR that the 'credit_judge_poc' directory itself is where the script resides,
    # and 'data', 'evaluation_poc' are subdirectories.
    # Adjust if project structure for running is different.
    
    ai_report_filename = "dkng_ai_report.json"
    gold_standard_filename = "dkng_review_table.json"

    # Construct full paths
    # If run_credit_judge_poc.py is in credit_judge_poc/
    ai_report_path = os.path.join(base_path, "data", "reports_to_be_judged", ai_report_filename)
    gold_standard_path = os.path.join(base_path, "data", "gold_standard_reviews", gold_standard_filename)
    
    print(f"AI Report Path: {ai_report_path}")
    print(f"Gold Standard Path: {gold_standard_path}")


    # --- 2. Load AI Report (Simulated LLM Output) ---
    print("\n--- Loading Simulated AI Report ---")
    # This step uses the parser we defined.
    # For the MVP, this loaded data IS the "LLM output".
    ai_report_data = load_ai_report_from_json(ai_report_path)
    if not ai_report_data:
        print("Failed to load AI report. Exiting.")
        return
    print(f"Successfully loaded AI report: {ai_report_filename}")
    # print("AI Report Data (snippet):")
    # print(json.dumps({k: v for k, v in list(ai_report_data.items())[:2]}, indent=2)) # Print first 2 items


    # --- 3. Format AI Output for Review ---
    print("\n--- Formatting AI Output for Review ---")
    # This step uses the formatter we defined.
    formatted_ai_output = format_ai_output_for_review(ai_report_data)
    if not formatted_ai_output:
        print("Failed to format AI output. Exiting.")
        return
    print("AI output formatted successfully.")
    # print("Formatted AI Output (snippet):")
    # print(json.dumps({k: v for k, v in list(formatted_ai_output.items())[:3]}, indent=2))


    # --- 4. Load Gold Standard Review ---
    print("\n--- Loading Gold Standard Review ---")
    gold_standard_data = load_gold_standard(gold_standard_path) # From evaluate_judge_outputs
    if not gold_standard_data:
        print("Failed to load Gold Standard review. Exiting.")
        return
    print(f"Successfully loaded Gold Standard review: {gold_standard_filename}")


    # --- 5. Evaluate Formatted AI Output against Gold Standard ---
    print("\n--- Evaluating AI Output against Gold Standard ---")
    
    # The evaluate_judge_outputs.py script expects a certain structure.
    # The `formatted_ai_output['comparable_sections']` is designed to fit this.
    # However, the current `dkng_ai_report.json` (and thus `formatted_ai_output`)
    # does not contain actual quantitative scores for sections that the gold standard *reviews*.
    # The gold standard *assigns* scores to the AI's sections.
    # So, `evaluate_report_sections` will mostly show "AI Score: Not Found/Not Applicable".
    # This is expected for the MVP, as we are not yet generating an AI report that self-scores in detail.

    # Compare overall scores (conceptual for MVP, as AI report doesn't self-score overall)
    ai_overall_score_from_formatted = None # Not present in current formatted_ai_output
    gold_overall_score = gold_standard_data.get("overallAssessment", {}).get("overallScore")
    
    print("Overall Score (from Gold Standard Review of AI Report):")
    compare_scores(ai_overall_score_from_formatted, gold_overall_score, "Overall Report (Gold Standard's View)")

    # Compare sections based on the structure from formatted_ai_output and gold_standard_data
    # The `formatted_ai_output.get('comparable_sections', {})` provides the AI's data in a way
    # `evaluate_report_sections` can try to map against the gold standard's section reviews.
    evaluate_report_sections(
        formatted_ai_output.get('comparable_sections', {}), # AI's data for comparison
        gold_standard_data.get("sectionReviews", [])      # Gold standard's review sections
    )
    
    print("\n--- Qualitative Summary from Formatted AI Output (for context) ---")
    print(f"Company: {formatted_ai_output.get('companyName')}")
    print(f"Inferred Rating by AI: {formatted_ai_output.get('inferredRating')} {formatted_ai_output.get('outlook')}")
    print(f"Key Strengths Noted by AI: {', '.join(formatted_ai_output.get('keyStrengthsSummary', []))}")
    print(f"Key Weaknesses Noted by AI: {', '.join(formatted_ai_output.get('keyWeaknessesSummary', []))}")


    # --- Conceptual: Next Steps/Further Iteration ---
    # - Integrate actual LLM calls.
    # - Enhance parser for different input report formats.
    # - Make formatter create richer, more structured comparison tables.
    # - Add more sophisticated NLP-based comparisons in evaluation.
    # - Implement detailed quantitative metric calculations (accuracy, MSE for scores if AI self-scores).

    print("\nCredit Judge PoC - MVP Run Completed.")

if __name__ == "__main__":
    # This allows the script to be run directly.
    # Ensure that the working directory is the root of the 'credit_judge_poc' project
    # or adjust paths accordingly if running from within the 'src' or other subdirectories.
    # Example: If in project root, run `python credit_judge_poc/run_credit_judge_poc.py`
    # If `credit_judge_poc` is in PYTHONPATH, can run `python -m credit_judge_poc.run_credit_judge_poc`
    main()
```

