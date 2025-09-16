import json
import textwrap

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

def display_qualitative_comparison(ai_report_data, gold_standard_data):
    """
    Displays a side-by-side qualitative comparison of the AI report
    and the gold standard review.
    """
    print("\n" + "="*80)
    print(" " * 25 + "Qualitative Comparison Report")
    print("="*80 + "\n")

    # --- Overall Assessment ---
    overall_assessment = gold_standard_data.get("overallAssessment", {})
    print("--- Overall Assessment of AI Report ---")
    print(f"Reviewer: {gold_standard_data.get('reviewerName', 'N/A')}")
    print(f"Overall Score by Reviewer: {overall_assessment.get('overallScore', 'N/A')}/10")
    print(f"Rating Concurrence: {overall_assessment.get('ratingConcurrence', 'N/A')}")
    print("\nReviewer's General Comments:")
    comments = overall_assessment.get('comments', 'No comments provided.')
    print(textwrap.fill(comments, width=80))
    print("-" * 80 + "\n")

    # --- Section-by-Section Comparison ---
    print("--- Section-by-Section Detailed Review ---\n")

    # Mapping from review sectionName to keys in the AI report JSON
    section_to_ai_key_map = {
        "Overview": "overview",
        "Corporate Credit Rating": "corporateCreditRating",
        "Financial Performance": "financialPerformance",
        "SNCF Regulatory Rating": "sncfRegulatoryRating",
        "Strengths": "strengths",
        "Weaknesses": "weaknesses",
        "Special Focus Areas": "specialFocusAreas"
    }

    for review_section in gold_standard_data.get("sectionReviews", []):
        section_name = review_section.get("sectionName")
        ai_key = section_to_ai_key_map.get(section_name)

        print(f"## Section: {section_name}\n")

        # --- Print Gold Standard Feedback ---
        print("  --- Gold Standard Review --")
        score = review_section.get('quantitativeScore')
        feedback = review_section.get('qualitativeFeedback', 'No feedback.')
        completeness = review_section.get('completeness')

        print(f"  Score: {score}/10" if score is not None else "  Score: N/A")
        if completeness is not None:
            print(f"  Completeness: {completeness}/10")
        print("  Feedback:")
        print(textwrap.fill(f"  > {feedback}", width=78, subsequent_indent='    '))
        print("\n")

        # --- Print AI Report Content ---
        print("  --- Corresponding AI Report Content --")
        if ai_key and ai_key in ai_report_data:
            ai_content = ai_report_data[ai_key]
            # Pretty print JSON/dict content, handle lists and strings
            if isinstance(ai_content, dict):
                content_str = json.dumps(ai_content, indent=2)
            elif isinstance(ai_content, list):
                content_str = "- " + "\n- ".join(ai_content)
            else: # It's a string
                content_str = textwrap.fill(ai_content, width=70)

            # Indent the whole block for clarity
            indented_content = "  " + content_str.replace("\n", "\n  ")
            print(indented_content)
        else:
            print("  Content not found in AI report for this section.")

        print("\n" + "-"*80 + "\n")
