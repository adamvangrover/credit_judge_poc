# Functions to format the Credit Judge LLM's output.
# Structures the LLM's qualitative feedback and scores into the desired table format (e.g., JSON, markdown).

import json

def format_ai_output_for_review(ai_report_data: dict):
    """
    Formats the AI-generated report data into a simplified structure for review or comparison.

    For the MVP, this extracts a few key fields. This function would be expanded
    to create more comprehensive and structured outputs in later iterations.

    Args:
        ai_report_data (dict): The AI-generated report data (e.g., loaded from dkng_ai_report.json).

    Returns:
        dict: A simplified dictionary containing key extracted information, or None if input is invalid.
    """
    if not ai_report_data or not isinstance(ai_report_data, dict):
        print("Error: Invalid input data for formatting.")
        return None

    formatted_review = {}

    # Extract company information
    formatted_review['companyName'] = ai_report_data.get('companyName', 'N/A')
    formatted_review['tickerSymbol'] = ai_report_data.get('tickerSymbol', 'N/A')
    formatted_review['assessmentDate'] = ai_report_data.get('assessmentDate', 'N/A')

    # Extract core credit rating assessment
    credit_rating_info = ai_report_data.get('corporateCreditRating', {})
    formatted_review['inferredRating'] = credit_rating_info.get('rating', 'N/A')
    formatted_review['outlook'] = credit_rating_info.get('outlook', 'N/A')
    formatted_review['ratingJustificationSummary'] = credit_rating_info.get('justification', 'N/A')[:200] + "..." # Summary

    # Extract a summary of strengths (example: first two strengths)
    strengths = ai_report_data.get('strengths', [])
    formatted_review['keyStrengthsSummary'] = strengths[:2] if strengths else ["N/A"]
    
    # Extract a summary of weaknesses (example: first two weaknesses)
    weaknesses = ai_report_data.get('weaknesses', [])
    formatted_review['keyWeaknessesSummary'] = weaknesses[:2] if weaknesses else ["N/A"]

    # Placeholder for quantitative scores if AI report included section self-scores
    # This would be populated if the AI output itself contained structured scores per section.
    # For the current 'dkng_ai_report.json', these are not present.
    formatted_review['section_scores_from_ai'] = {
        # "OverviewAccuracy": ai_report_data.get("overview", {}).get("self_assessed_accuracy_score"),
        # "FinancialsComprehensiveness": ai_report_data.get("financialPerformance", {}).get("self_assessed_comprehensiveness_score")
    }


    # --- Conceptual: Placeholder for how one might structure for direct comparison ---
    # This is what evaluate_judge_outputs.py might expect for its `ai_sections_for_comparison`
    # This requires knowing what the gold standard sections are named.
    # For now, this is illustrative.
    formatted_review['comparable_sections'] = {
        "Corporate Credit Rating": {"quantitativeScore": None}, # No direct score in dkng_ai_report.json for this
        "Financial Performance": {"quantitativeScore": None},
        "Strengths": {"qualitativeSummary": strengths[:2]},
        "Weaknesses": {"qualitativeSummary": weaknesses[:2]}
        # Add other sections if they are to be directly compared and AI provides data.
    }
    # Example: If AI report had a financial data accuracy score (conceptual)
    # if 'financialPerformance' in ai_report_data and 'dataAccuracyScore' in ai_report_data['financialPerformance']:
    #    formatted_review['comparable_sections']['Financial Performance']['quantitativeScore'] = ai_report_data['financialPerformance']['dataAccuracyScore']


    return formatted_review

# Example Usage:
# if __name__ == '__main__':
#     # This example would typically be run from a higher-level script
#     # For direct testing, you'd need to load data first.
#     example_ai_data = {
#         "reportTitle": "AI-Generated Corporate Credit Assessment: DraftKings Inc. (DKNG)",
#         "assessmentDate": "2024-10-28",
#         "companyName": "DraftKings Inc.",
#         "tickerSymbol": "DKNG",
#         "corporateCreditRating": {
#             "rating": "B+",
#             "outlook": "Stable",
#             "justification": "The 'B+' rating reflects DraftKings' significant revenue scale..."
#         },
#         "strengths": ["Leading market share", "Strong brand recognition"],
#         "weaknesses": ["History of GAAP net losses", "High marketing spend"]
#         # ... other fields from dkng_ai_report.json
#     }
#     
#     formatted_output = format_ai_output_for_review(example_ai_data)
#     
#     if formatted_output:
#         print("Formatted AI Output for Review:")
#         print(json.dumps(formatted_output, indent=2))
#     else:
#         print("Failed to format AI output.")

