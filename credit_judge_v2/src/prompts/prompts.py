# This file contains the prompt templates for the Credit Judge v2 system.

# This is a simplified version of the prompt for generating a corporate credit rating report.
# In a real application, this would be much more detailed and might include few-shot examples.
REPORT_GENERATION_PROMPT = """
**Objective:** Generate a comprehensive Corporate Credit Rating Report.

**Company Information:**
*   **Company Name:** {company_name}
*   **Ticker Symbol:** {ticker_symbol}

**Instructions:**
Based on the provided company information, generate a structured JSON report with the following sections:
- reportTitle
- assessmentDate
- companyName
- tickerSymbol
- overview
- corporateCreditRating (including rating, outlook, and justification)
- financialPerformance (including revenue, EBITDA, FCF, and leverage)
- sncfRegulatoryRating (indicative rating and justification)
- strengths (list of strings)
- weaknesses (list of strings)
- specialFocusAreas (list of strings)

The report should be well-researched, accurate, and professionally written.
The output must be a single, valid JSON object.
"""

def get_report_generation_prompt(company_name, ticker_symbol):
    """
    Formats the main report generation prompt with the given company details.
    """
    return REPORT_GENERATION_PROMPT.format(
        company_name=company_name,
        ticker_symbol=ticker_symbol
    )
