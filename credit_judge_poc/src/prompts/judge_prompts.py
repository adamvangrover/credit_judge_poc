# Stores and manages prompt templates for the Credit Judge LLM.
# Contains base prompts, section-specific instructions, scoring rubrics, and few-shot examples.

# credit_judge_poc/src/prompts/judge_prompts.py

CORPORATE_CREDIT_RATING_REPORT_TEMPLATE = """
**Objective:** Generate a Corporate Credit Rating Report for the specified company. If a human example is provided, also compare the AI-generated report to it and provide a performance score.

**I. Company Information:**

*   **Company Name:** {{company_name}}
*   **Ticker Symbol:** {{ticker_symbol}}
*   **(Optional) Primary Stock Exchange:** {{stock_exchange}}

**II. AI Report Generation Instructions:**

A.  **Information Gathering (Simulate using Google Search):**
    *   **Objective:** Find the latest publicly available information (as of {{current_date}}) for the company covering:
        1.  **Overall Business:** Industry, core operations, market position, primary products/services.
        2.  **Recent Financial Performance:**
            *   Latest reported quarter (e.g., Q1 2025, Q4 2024) and fiscal year-end.
            *   Revenue (latest quarter & FY, YoY growth).
            *   EBITDA or Adjusted EBITDA (latest quarter & FY, trends, margins).
            *   Net Income (latest quarter & FY, trends).
            *   Free Cash Flow (latest available, trend).
            *   Key Leverage Metrics (e.g., Debt-to-EBITDA, Net Debt, Cash & Equivalents).
        3.  **Existing Credit Ratings:** Public ratings and outlooks from S&P, Moody's, Fitch (if available).
        4.  **Key Strengths & Competitive Advantages.**
        5.  **Key Weaknesses & Risks:** Operational, financial, market, regulatory.
        6.  **Recent Material News:** M&A, major product developments, significant regulatory impacts.

B.  **Specific Financial Data Overrides (Use these figures if provided, instead of search findings for these items):**
    *   Reporting Period for Override Data: {{specific_financial_period_override}}
    *   Revenue: {{specific_revenue_override}}
    *   Adjusted EBITDA: {{specific_adj_ebitda_override}}
    *   Net Income: {{specific_net_income_override}}
    *   Free Cash Flow: {{specific_fcf_override}}
    *   Other Data (Specify): {{specific_other_data_override}}
    *(Note: If any override field above is blank or "N/A", rely on search for that item.)*

C.  **Report Structure to Generate:**
    *   **I. Overview:** Description of the company, its industry, recent performance highlights, and key challenges.
    *   **II. Corporate Credit Rating:**
        *   S&P Equivalent Scale: [Infer a rating, e.g., AAA, AA+, ... D]
        *   Outlook: [Stable, Positive, Negative, Developing]
        *   Justification and Rationale: Detailed explanation for the rating and outlook.
        *   Outlook (Detailed): Specific factors/triggers for potential upgrade or downgrade.
    *   **III. Financial Performance (using latest found data or provided overrides):**
        *   Revenue: (Amount, period, YoY growth, key drivers).
        *   EBITDA: (Amount, period, margin, trends, key drivers).
        *   Free Cash Flow: (Amount, period, trend, significance).
        *   Leverage: (Key ratios like Debt/EBITDA, net debt, cash position, liquidity, debt structure insights).
    *   **IV. Shared National Credit (SNC) Regulatory Rating (Indicative):**
        *   SNC Indicative Rating: [Infer: Pass, Special Mention, Substandard based on public risk profile vs. general SNC criteria]
        *   Justification and Rationale: Explanation for the indicative SNC classification.
        *   Triggers: Potential conditions for a change in this indicative classification.
        *   Strengths: Bulleted list of key company strengths.
        *   Weaknesses: Bulleted list of key company weaknesses.

D.  **(Optional) Special Focus Areas:** {{special_focus_areas}}

**III. Comparison and Scoring (Perform only if Human Example Report is provided below):**

*   **Human Example Report Text for {{company_name}}:**
    ```
    {{human_example_report_text}}
    ```
    *(If the text above is blank or "N/A", skip comparison and scoring.)*

*   **If Human Example is Provided:**
    1.  **Comparison Table:** Create a table comparing your AI-generated report (section by section) against the provided human example. Note alignments, data differences (especially if periods differ), and qualitative nuances.
    2.  **Performance Score:** Score your AI report against the human example (0-10 scale for each, then an overall average):
        *   Adherence to Format & Structure (if human example implies a specific structure)
        *   Accuracy/Comparability of Data (considering reported periods)
        *   Quality of Rationale & Justification
        *   Coverage of Key Themes
        *   Clarity & Professionalism
        *   Overall Score

**IV. Confirmation:**
*   Acknowledge that Google Search will be simulated for information gathering.
*   Confirm understanding of limitations regarding non-public data and official rating assignments.
"""

# Example of how to use it (likely in a notebook or main script):
# from .judge_prompts import CORPORATE_CREDIT_RATING_REPORT_TEMPLATE
# import datetime
#
# final_prompt = CORPORATE_CREDIT_RATING_REPORT_TEMPLATE.format(
# company_name="ExampleCorp",
# ticker_symbol="EXMPL",
# stock_exchange="NYSE",
# current_date=datetime.date.today().strftime("%Y-%m-%d"),
# specific_financial_period_override="N/A",
# specific_revenue_override="N/A",
# specific_adj_ebitda_override="N/A",
# specific_net_income_override="N/A",
# specific_fcf_override="N/A",
# specific_other_data_override="N/A",
# special_focus_areas="Impact of new regulations.",
# human_example_report_text="N/A" # Or actual human report text
# )
# print(final_prompt)


SIMULATED_INPUT_REPORT_TEMPLATE = """
**Objective:** Generate a simulated RAG-style compilation of retrieved text snippets for a given company, intended to be used as source material for a full credit analysis.

**Company Name:** {{company_name}}
**Ticker Symbol:** {{ticker_symbol}}
**(Optional) Industry:** {{industry}}
**(Optional) Key Aspects to Focus On (e.g., recent M&A, specific product line):** {{focus_areas}}

**Instructions:**
Based on the company information provided above, generate a series of text snippets that would typically be retrieved from various sources (e.g., earnings call transcripts, annual reports, industry analyst reports, news articles) to inform a credit assessment.
The output should be structured into the following sections. Each snippet should ideally mention a hypothetical source or type of source.

**I. Business Overview Snippets:**
*   (Generate 2-3 snippets describing the company's core operations, market position, primary products/services. Include hypothetical source attribution.)
*   Example Snippet: "*Source: Company FY23 Annual Report* - '[Company Name] is a leading provider of [products/services] in the [industry] sector...'"

**II. Financial Performance Snippets:**
*   (Generate 2-3 snippets highlighting recent financial results, key metrics, or trends. Include hypothetical source attribution and mention reporting periods like 'Q3 2024' or 'FY2023'.)
*   Example Snippet: "*Source: Q3 2024 Earnings Call Transcript* - 'Revenue for the third quarter was [amount], an increase of [percentage]% year-over-year, driven by strong performance in our [segment] segment...' - CFO, [Company Name]"

**III. Key Strengths Snippets (from various hypothetical sources):**
*   (Generate 2-3 snippets that would indicate company strengths from different perspectives like market leadership, innovation, financial stability. Include hypothetical source attribution.)
*   Example Snippet: "*Source: Industry Analyst Report - [Sector] Q1 2024* - '[Company Name] benefits from a strong brand and extensive distribution network, providing a significant competitive advantage.'"

**IV. Key Weaknesses/Risks Snippets (from various hypothetical sources):**
*   (Generate 2-3 snippets that would indicate company weaknesses or risks, such as competition, regulatory issues, operational challenges. Include hypothetical source attribution.)
*   Example Snippet: "*Source: Financial News Article - [Date]* - 'Analysts express concern over [Company Name]'s increasing debt load in a rising interest rate environment...'"

**V. Recent Material News/Events Snippets:**
*   (Generate 1-2 snippets about recent significant news, M&A activity, product launches, or regulatory developments. Include hypothetical source attribution.)
*   Example Snippet: "*Source: Press Release - [Date]* - '[Company Name] today announced the successful acquisition of [Acquired Company], which is expected to [strategic impact].'"

**Output Format:**
Maintain the section headings (I, II, III, IV, V) as provided. Use bullet points for individual snippets within each section.
Ensure the content is plausible for the given company and focus areas.
The language should be indicative of retrieved text, not overly polished or analytical itself.
"""

# Example of how to use the new template (for testing, likely in a notebook):
# from .judge_prompts import SIMULATED_INPUT_REPORT_TEMPLATE
#
# filled_simulated_input_prompt = SIMULATED_INPUT_REPORT_TEMPLATE.format(
#     company_name="ExampleTech Inc.",
#     ticker_symbol="EXTI",
#     industry="Software and Cloud Services",
#     focus_areas="Recent AI product launches and their market reception"
# )
# print(filled_simulated_input_prompt)


EXPERT_REVIEW_TABLE_GENERATION_TEMPLATE = """
**Objective:** Generate an expert human-style review table in JSON format for a given credit report.
You are acting as a seasoned credit analyst. Your task is to critically evaluate the provided credit report.

**Input Credit Report to be Reviewed:**
```text
{{input_credit_report_text}}
```

**Instructions for Review and JSON Output Structure:**

Based on the "Input Credit Report to be Reviewed" above, generate a single JSON object that follows the structure outlined below.
Provide thoughtful qualitative feedback and assign quantitative scores where indicated. Scores should generally be on a 0-10 scale, where 10 is outstanding.

**JSON Output Structure:**

```json
{
  "reviewedReportId": "{{report_id_placeholder}}", // e.g., "DKNG-AI-Report-2024-Q3" or a hash of the report
  "reviewerName": "AI Credit Review Expert", // Or a more specific persona if desired
  "reviewDate": "{{current_date}}",
  "overallAssessment": {
    "comments": "[Provide a detailed overall assessment of the input credit report. Discuss its strengths, weaknesses, clarity, depth of analysis, and any major omissions or inaccuracies. Aim for 2-4 sentences.]",
    "overallScore": "[Assign an overall numerical score from 0-10 for the input report.]",
    "ratingConcurrence": "[If the input report proposed a credit rating, state whether you 'Strongly Agree', 'Agree', 'Neutral', 'Disagree', or 'Strongly Disagree' with the inferred rating and its justification. If no rating was proposed, state 'N/A'.]"
  },
  "sectionReviews": [
    // For each major section identified in the input credit report (e.g., Overview, Financial Performance, Strengths, Weaknesses, Credit Rating Rationale, etc.),
    // create a JSON object with the following structure.
    // Adapt the "sectionName" to match the actual sections found in the input report.
    {
      "sectionName": "[Name of the section from the input report, e.g., 'Business Overview', 'Financial Performance Analysis', 'Corporate Credit Rating Justification']",
      "qualitativeFeedback": "[Provide specific feedback on this section. Comment on its accuracy, completeness, clarity, and analytical depth. What was done well? What could be improved? Aim for 1-3 sentences.]",
      "quantitativeScore": "[Assign a numerical score (0-10) for the quality of this specific section.]",
      "dataAccuracy": "[If applicable to the section, score (0-10) the perceived accuracy of the data presented. If not applicable, use 'N/A'.]",
      "completeness": "[Score (0-10) how complete the information and analysis are for this section's typical scope. If not applicable, use 'N/A'.]",
      "analyticalDepth": "[If applicable, score (0-10) the depth of analysis and insight provided in this section. If not applicable, use 'N/A'.]"
    }
    // Add more section review objects as needed to cover all major parts of the input report.
    // Example for a second section:
    // {
    //   "sectionName": "Financial Performance",
    //   "qualitativeFeedback": "...",
    //   "quantitativeScore": ...,
    //   "dataAccuracy": ...,
    //   "completeness": ...,
    //   "analyticalDepth": ...
    // }
  ]
}
```

**Guidelines for Review Content:**
-   **Be Critical but Fair:** Identify both strengths and areas for improvement in the input report.
-   **Be Specific:** Refer to specific aspects of the report in your feedback.
-   **Adhere to JSON Format:** Ensure the final output is a single, valid JSON object as specified.
-   **Placeholder Values:** Replace bracketed placeholders like `[Provide detailed overall assessment...]` with your actual evaluation. For `{{report_id_placeholder}}` and `{{current_date}}`, these will be substituted by the system calling the prompt.
"""

# Example of how to use the new template (for testing, likely in a notebook):
# from .judge_prompts import EXPERT_REVIEW_TABLE_GENERATION_TEMPLATE
# import datetime
#
# # This would be the text of the AI-generated report you want to review
# example_input_report_for_review = """
# **I. Overview:** ExampleCorp is a leading widget manufacturer.
# **II. Financials:** Revenue $100M. Net Income $10M.
# ... (rest of a hypothetical report) ...
# """
#
# filled_expert_review_prompt = EXPERT_REVIEW_TABLE_GENERATION_TEMPLATE.format(
#     input_credit_report_text=example_input_report_for_review,
#     report_id_placeholder="ExampleCorp-Report-001",
#     current_date=datetime.date.today().strftime("%Y-%m-%d")
# )
# print(filled_expert_review_prompt)


COMPARISON_TABLE_GENERATION_TEMPLATE = """
**Objective:** Generate a detailed Markdown comparison table and performance score assessing an AI-generated credit report against a human expert example report.

**Instructions:**
You are provided with two credit reports for the same company:
1.  An "AI-Generated Report."
2.  A "Human Expert Example Report."

Your task is to:
1.  Perform a section-by-section comparison of these two reports.
2.  Create a detailed comparison table in Markdown format.
3.  Provide a performance score for the AI-Generated Report based on the comparison, using a 0-10 scale for various criteria.

**Input Data:**

*   **Company Name:** {{company_name}}
*   **AI-Generated Report Text:**
    ```text
    {{ai_generated_report_text}}
    ```
*   **Human Expert Example Report Text:**
    ```text
    {{human_expert_report_text}}
    ```

**Output Structure:**

Your output should be a single, well-formatted Markdown document.

**Part 1: Comparison Table**

Create a Markdown table with the following columns:
| Section         | AI Report Summary & Key Points | Human Expert Report Summary & Key Points | Alignment & Differences Noted (Data, Nuances, Omissions) |
|-----------------|--------------------------------|------------------------------------------|----------------------------------------------------------|
| *(e.g. Overview)* | *(Summarize AI's overview)*  | *(Summarize Expert's overview)*          | *(Comment on similarities, differences in scope, data, emphasis, any omissions by AI)* |
| *(e.g. Corporate Credit Rating)* | *(AI's rating, outlook, key rationale points)* | *(Expert's rating, outlook, key rationale points)* | *(Compare ratings, outlooks. Note differences in justification logic, depth, specific factors mentioned)* |
| *(e.g. Financial Performance - Revenue)* | *(AI's revenue figures, period, growth, drivers)* | *(Expert's revenue figures, period, growth, drivers)* | *(Directly compare data. Note any discrepancies in figures, periods, or interpretation of drivers. Highlight if AI missed key context provided by expert.)* |
| *(...continue for all relevant sections like EBITDA, FCF, Leverage, SNC Rating, Strengths, Weaknesses, Special Focus Areas, etc.)* | | | |

**Guidelines for Comparison Table Content:**
*   **Be Thorough:** Cover all major corresponding sections from both reports. If one report has a section the other doesn't, note it.
*   **Be Specific:** In "Alignment & Differences," quote or refer to specific data points, phrases, or analytical conclusions.
*   **Consider Data Periods:** If financial data periods differ, explicitly state this and assess comparability accordingly.
*   **Qualitative Nuances:** Note differences in tone, emphasis, depth of analysis, or any unique insights provided by either report.

**Part 2: Performance Score of AI Report (vs. Human Expert Example)**

Below the table, provide a "Performance Score" section. Score the AI-Generated Report against the Human Expert Example report using a 0-10 scale for each of the following criteria. Provide a brief justification for each score.

*   **Adherence to Format & Structure (if human example implies a specific structure):** [Score/10]
    *   *Justification:* ...
*   **Accuracy/Comparability of Data (considering reported periods):** [Score/10]
    *   *Justification:* ...
*   **Quality of Rationale & Justification (e.g., for ratings, conclusions):** [Score/10]
    *   *Justification:* ...
*   **Coverage of Key Credit Themes & Risks:** [Score/10]
    *   *Justification:* ...
*   **Clarity, Professionalism & Readability:** [Score/10]
    *   *Justification:* ...
*   **Overall Score (Average or Weighted):** [Calculate and state overall score/10]
    *   *Brief Overall Summary:* ...

**Final Output:**
Ensure the entire output is valid Markdown.
"""

# Example of how to use the new template (for testing, likely in a notebook):
# from .judge_prompts import COMPARISON_TABLE_GENERATION_TEMPLATE
#
# # These would be the full text of the reports
# example_ai_report = "Overview: AI says A. Financials: AI says revenue is $1B."
# example_human_expert_report = "Overview: Expert says B. Financials: Expert says revenue is $1.1B for same period."
#
# filled_comparison_prompt = COMPARISON_TABLE_GENERATION_TEMPLATE.format(
#     company_name="ExampleCorp",
#     ai_generated_report_text=example_ai_report,
#     human_expert_report_text=example_human_expert_report
# )
# print(filled_comparison_prompt)
