# Functions to format the AI's output into a structured, comparable format.

def format_ai_output_for_review(ai_report_data):
    """
    Formats the raw AI report dictionary into a more structured format
    for summary and comparison.

    Args:
        ai_report_data (dict): The raw dictionary loaded from the AI report JSON.

    Returns:
        dict: A dictionary containing formatted, easily accessible fields.
    """
    if not ai_report_data:
        return None

    # Extract high-level info
    company_name = ai_report_data.get("companyName", "N/A")
    rating_info = ai_report_data.get("corporateCreditRating", {})
    inferred_rating = rating_info.get("rating", "N/A")
    outlook = rating_info.get("outlook", "N/A")

    # Extract summaries of strengths and weaknesses
    strengths_summary = ai_report_data.get("strengths", [])
    weaknesses_summary = ai_report_data.get("weaknesses", [])

    # This mapping is crucial for the evaluation script to find the
    # corresponding sections in the AI report. The keys match the
    # 'sectionName' in the gold standard review table.
    comparable_sections = {
        "Overview": {"content": ai_report_data.get("overview")},
        "Corporate Credit Rating": {"content": ai_report_data.get("corporateCreditRating")},
        "Financial Performance": {"content": ai_report_data.get("financialPerformance")},
        "SNCF Regulatory Rating": {"content": ai_report_data.get("sncfRegulatoryRating")},
        "Strengths": {"content": strengths_summary},
        "Weaknesses": {"content": weaknesses_summary},
        "Special Focus Areas": {"content": ai_report_data.get("specialFocusAreas")}
    }

    formatted_output = {
        "companyName": company_name,
        "inferredRating": inferred_rating,
        "outlook": outlook,
        "keyStrengthsSummary": strengths_summary,
        "keyWeaknessesSummary": weaknesses_summary,
        "comparable_sections": comparable_sections
    }

    return formatted_output
