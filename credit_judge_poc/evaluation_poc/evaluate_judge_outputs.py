# Scripts to evaluate the performance of the Credit Judge LLM.
# Compares LLM-generated review tables against 'gold_standard_reviews' and calculates metrics.
#<<<<<<< initial-scaffold

import json
import os

def load_json_file(filepath):
    """Loads a JSON file from the given filepath."""
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return None

def compare_scores(ai_score, gold_score, section_name="Overall"):
    """Compares two scores and prints the comparison."""
    print(f"--- {section_name} Score Comparison ---")
    print(f"  AI Generated Score: {ai_score}")
    print(f"  Gold Standard Score: {gold_score}")
    if isinstance(ai_score, (int, float)) and isinstance(gold_score, (int, float)):
        difference = abs(ai_score - gold_score)
        print(f"  Difference: {difference:.2f}")
    else:
        print("  Cannot calculate numerical difference for non-numeric scores.")
    print("\n")

def evaluate_report_sections(ai_report_sections_map, gold_standard_sections_list):
    """Compares scores for aligned sections from AI report and gold standard."""
    if not ai_report_sections_map or not gold_standard_sections_list:
        print("Missing section data for comparison.\n")
        return

    print("--- Section-by-Section Review ---")
    
    num_comparable_sections = 0
    total_score_difference = 0
    # Placeholder for Mean Squared Error calculation
    # total_squared_error = 0 

    for gold_section in gold_standard_sections_list:
        gold_section_name = gold_section.get('sectionName')
        gold_score = gold_section.get('quantitativeScore')

        ai_section_data = ai_report_sections_map.get(gold_section_name)
        ai_score = None

        if ai_section_data and 'quantitativeScore' in ai_section_data:
            ai_score = ai_section_data.get('quantitativeScore')

        print(f"Section: {gold_section_name}")
        if ai_score is not None and gold_score is not None:
            print(f"  AI Score: {ai_score} | Gold Score: {gold_score}")
            if isinstance(ai_score, (int, float)) and isinstance(gold_score, (int, float)):
                difference = abs(ai_score - gold_score)
                print(f"  Difference: {difference:.2f}")
                total_score_difference += difference
                # total_squared_error += difference**2 # For MSE
                num_comparable_sections +=1
            else:
                print("  Non-numeric score(s), cannot calculate difference.")
        elif gold_score is not None:
            print(f"  AI Score: Not Found/Not Applicable | Gold Score: {gold_score}")
        else:
            print(f"  AI Score: {ai_score if ai_score is not None else 'Not Found'} | Gold Score: Not Available")
        print("-" * 20)

    if num_comparable_sections > 0:
        mean_score_difference = total_score_difference / num_comparable_sections
        print(f"Mean Absolute Difference across {num_comparable_sections} comparable sections: {mean_score_difference:.2f}\n")
        # mse = total_squared_error / num_comparable_sections
        # print(f"Mean Squared Error across {num_comparable_sections} comparable sections: {mse:.2f}\n")
    else:
        print("No comparable sections with quantitative scores found for difference calculation.\n")

    # --- Placeholder for Advanced Text Comparison ---
    # For qualitative feedback, one could use NLP techniques:
    # - Cosine similarity of embeddings (e.g., using Sentence Transformers) for qualitativeFeedback fields.
    # - Topic modeling to compare themes discussed in justifications or overviews.
    # - Sentiment analysis comparison on qualitative statements.
    print("--- Conceptual: Advanced Text Comparison (Qualitative Fields) ---")
    print("To implement advanced text comparison:")
    print("1. Extract qualitative text from AI report sections (e.g., 'justification', 'overview', 'keyDrivers').")
    print("2. Extract corresponding qualitative text from gold standard review ('qualitativeFeedback').")
    print("3. Use NLP libraries (e.g., scikit-learn for TF-IDF, Sentence Transformers for embeddings) to compare.")
    print("   Example: Calculate cosine similarity between AI's justification for a rating and gold standard's feedback.\n")


def main():
    base_path = os.path.dirname(__file__)
    # Path to the AI-generated report (this is the *subject* of the review)
    ai_report_path = os.path.join(base_path, "..", "data", "reports_to_be_judged", "dkng_ai_report.json")
    # Path to the gold standard review *of the AI report*
    gold_standard_review_path = os.path.join(base_path, "..", "data", "gold_standard_reviews", "dkng_review_table.json")

    ai_report_content = load_json_file(ai_report_path)
    gold_standard_review_content = load_json_file(gold_standard_review_path)

    if not ai_report_content or not gold_standard_review_content:
        print("Exiting due to load errors.")
        return

    # --- Overall Assessment Score (from Gold Standard Review) ---
    # This score is the human expert's overall rating of the AI-generated report.
    gold_overall_assessment = gold_standard_review_content.get("overallAssessment", {})
    gold_overall_score = gold_overall_assessment.get("overallScore")
    gold_overall_comments = gold_overall_assessment.get("comments")

    print("--- Evaluation of AI-Generated Report (DKNG) ---")
    print(f"Gold Standard Reviewer's Overall Score for the AI Report: {gold_overall_score if gold_overall_score is not None else 'Not Provided'}")
    print(f"Reviewer Comments: {gold_overall_comments if gold_overall_comments else 'No comments.'}\n")
    
    # --- Section-Level Comparison ---
    # The `dkng_ai_report.json` (ai_report_content) has primary sections like "corporateCreditRating", "financialPerformance".
    # The `dkng_review_table.json` (gold_standard_review_content) has `sectionReviews` which are evaluations of *those AI sections*.
    # We need to map the `sectionName` from the review table to the corresponding section in the AI report
    # if we were to compare AI's self-assessment (which is not present) or specific data points.

    # For this script, the `quantitativeScore` in `gold_standard_review_content.sectionReviews`
    # is the expert's score *for that section of the AI report*.
    # There isn't an equivalent "AI score" in `ai_report_content` for direct comparison in this setup.
    # What we *can* demonstrate is how the gold standard review itself is structured.

    print("--- Summary of Gold Standard Review Scores for AI Report Sections ---")
    gold_section_reviews = gold_standard_review_content.get("sectionReviews", [])
    if not gold_section_reviews:
        print("No section reviews found in the gold standard table.")
    else:
        for review_item in gold_section_reviews:
            section_name = review_item.get("sectionName")
            quant_score = review_item.get("quantitativeScore")
            qual_feedback = review_item.get("qualitativeFeedback")
            print(f"Section: {section_name}")
            print(f"  Expert's Quantitative Score for AI's Section: {quant_score if quant_score is not None else 'N/A'}")
            print(f"  Expert's Qualitative Feedback: {qual_feedback if qual_feedback else 'N/A'}")
            print("-" * 20)
    print("\n")

    # --- Conceptual Comparison (if AI report had comparable scores/data) ---
    # To make `evaluate_report_sections` more meaningful, let's imagine the AI report *did* contain
    # its own quantitative assessments or specific extractable data points we want to score.
    # For example, if `ai_report_content.corporateCreditRating` had a field `confidenceScore`
    # and the gold standard review had a `quantitativeScore` for "Corporate Credit Rating" that
    # was meant to be compared against this `confidenceScore`.

    # This is a conceptual mapping to demonstrate the function.
    # In a real scenario, you'd parse specific fields from `ai_report_content`.
    conceptual_ai_sections_for_eval = {
        "Overview": {"quantitativeScore": None}, # AI report has an overview, but not a score for it
        "Corporate Credit Rating": {"quantitativeScore": None}, # AI infers a rating, but doesn't self-score its rationale quality
        "Financial Performance": {"quantitativeScore": None}, # AI provides data, doesn't score its presentation
        # Add other sections from `dkng_review_table.json` `sectionName`
        "SNCF Regulatory Rating": {"quantitativeScore": None},
        "Strengths": {"quantitativeScore": None},
        "Weaknesses": {"quantitativeScore": None},
        "Special Focus Areas": {"quantitativeScore": None}
    }
    # Example: If AI report's "corporateCreditRating" section had a "ratingValueNumeric" (e.g. B+ mapped to 11)
    # and gold_standard_review for "Corporate Credit Rating" had a "quantitativeScore" representing that same mapping.
    # conceptual_ai_sections_for_eval["Corporate Credit Rating"]["quantitativeScore"] = map_rating_to_numeric(ai_report_content.get("corporateCreditRating", {}).get("rating"))
    
    # This call will mostly show "AI Score: Not Found" because `dkng_ai_report.json` isn't structured for this direct comparison.
    # It serves to illustrate how the comparison function would work if the data was shaped differently.
    print("--- Conceptual Direct Score Comparison (Illustrative) ---")
    print("Illustrating comparison if AI report had directly comparable quantitative scores for its sections:")
    evaluate_report_sections(conceptual_ai_sections_for_eval, gold_section_reviews)


    # --- Placeholder for Probability Mapping of Scoring ---
    print("--- Conceptual: Probability Mapping of Scoring ---")
    print("This involves the LLM outputting probabilities for its assessments (e.g., P(Outlook=Stable)=0.7).")
    print("Evaluation would then compare these AI-generated probabilities against:")
    print("  a) Probabilities derived from gold-standard qualitative statements, or")
    print("  b) Actual outcomes if evaluating predictive accuracy over time.")
    print("Example: If AI stated 'Rating: B+ (0.8), A- (0.1), B (0.1)' and gold standard was 'B+', compare distributions.")
    print("Metrics: Brier Score, Log Probabilistic Score.\n")

    # --- Placeholder for Calculating Metrics like Mean Squared Error ---
    print("--- Conceptual: Advanced Metrics Calculation (beyond MAE) ---")
    print("If direct quantitative comparisons were made (as illustrated conceptually above):")
    print("- Mean Squared Error (MSE): Calculated in `evaluate_report_sections` if scores available.")
    print("- Accuracy for classifications: E.g., If AI classifies 'Outlook' as Positive/Stable/Negative, compare to gold standard classification.")
    print("  Accuracy = (Correct Classifications) / (Total Classifications)")
    print("- Precision/Recall/F1 for specific extracted items: E.g., if AI extracts 'Key Strengths' as a list,")
    print("  compare against gold standard list for precision (correct items extracted / total extracted by AI)")
    print("  and recall (correct items extracted / total in gold standard).\n")

if __name__ == "__main__":
    main()
```
=======
#>>>>>>> main
