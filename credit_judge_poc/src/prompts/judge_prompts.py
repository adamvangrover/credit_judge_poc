# Stores and manages prompt templates for the Credit Judge LLM.
# Contains base prompts, section-specific instructions, scoring rubrics, and few-shot examples.
#<<<<<<< initial-scaffold

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
=======
#>>>>>>> main
