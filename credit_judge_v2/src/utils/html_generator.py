import os
from datetime import datetime

def generate_html_report(ai_report, analysis_results, gold_standard, output_path="credit_judge_v2/output/report.html"):
    """
    Generates an HTML report by filling in the template with data.
    """

    # 1. Load Template
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, "report_template.html")

    try:
        with open(template_path, 'r') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Template not found at {template_path}")
        return

    # 2. Prepare Data for Replacement

    # Basic Info
    company_name = ai_report.get("companyName", "N/A")
    ticker_symbol = ai_report.get("tickerSymbol", "N/A")
    generation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Executive Summary
    rating_info = ai_report.get("corporateCreditRating", {})
    rating = rating_info.get("rating", "N/A")
    outlook = rating_info.get("outlook", "N/A")
    rating_justification = rating_info.get("justification", "N/A")

    sncf_info = ai_report.get("sncfRegulatoryRating", {})
    sncf_rating = sncf_info.get("indicativeRating", "N/A")
    sncf_justification = sncf_info.get("justification", "N/A")

    overview = ai_report.get("overview", "N/A")

    # Quantitative Metrics
    sentiment_polarity = f"{analysis_results['sentiment']['polarity']:.2f}"
    sentiment_subjectivity = f"{analysis_results['sentiment']['subjectivity']:.2f}"
    readability_score = f"{analysis_results['readability']:.2f}"
    numerical_density = f"{analysis_results['numerical_density']:.2f}"
    text_length = str(analysis_results['full_text_length'])

    keyword_badges = ""
    for kw, density in analysis_results['keyword_density'].items():
        if density > 0:
            keyword_badges += f'<span class="bg-red-100 text-red-800 text-xs font-medium mr-2 px-2.5 py-0.5 rounded">{kw}: {density:.1f}</span>'

    # Qualitative Comparison
    reviewer_comments = gold_standard.get("overallAssessment", {}).get("comments", "N/A")
    overall_score = str(gold_standard.get("overallAssessment", {}).get("overallScore", "N/A"))
    concurrence = gold_standard.get("overallAssessment", {}).get("ratingConcurrence", "N/A")

    comparison_rows = ""
    for section in gold_standard.get("sectionReviews", []):
        name = section.get("sectionName", "N/A")
        feedback = section.get("qualitativeFeedback", "N/A")
        score = section.get("quantitativeScore", "N/A")

        row = f"""
        <tr class="border-b hover:bg-gray-50">
            <td class="p-3 font-medium">{name}</td>
            <td class="p-3 text-gray-600">{feedback}</td>
            <td class="p-3 font-bold text-center bg-gray-100">{score}</td>
        </tr>
        """
        comparison_rows += row

    # 3. Replace Placeholders
    html_content = template
    replacements = {
        "{{ company_name }}": company_name,
        "{{ ticker_symbol }}": ticker_symbol,
        "{{ generation_date }}": generation_date,
        "{{ rating }}": rating,
        "{{ outlook }}": outlook,
        "{{ rating_justification }}": rating_justification,
        "{{ sncf_rating }}": sncf_rating,
        "{{ sncf_justification }}": sncf_justification,
        "{{ overview }}": overview,
        "{{ sentiment_polarity }}": sentiment_polarity,
        "{{ sentiment_subjectivity }}": sentiment_subjectivity,
        "{{ readability_score }}": readability_score,
        "{{ numerical_density }}": numerical_density,
        "{{ text_length }}": text_length,
        "{{ keyword_badges }}": keyword_badges,
        "{{ reviewer_comments }}": reviewer_comments,
        "{{ overall_score }}": overall_score,
        "{{ concurrence }}": concurrence,
        "{{ comparison_rows }}": comparison_rows
    }

    for key, value in replacements.items():
        html_content = html_content.replace(key, str(value))

    # 4. Save File
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_path, 'w') as f:
        f.write(html_content)

    print(f"\nHTML Report successfully generated at: {output_path}")
