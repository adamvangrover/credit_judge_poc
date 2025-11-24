import os
import json
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_mock_response(company_name, ticker):
    if "Tesla" in company_name:
        return {
            "reportTitle": f"AI-Generated Corporate Credit Assessment: {company_name} ({ticker})",
            "assessmentDate": "2025-05-15",
            "companyName": company_name,
            "tickerSymbol": ticker,
            "overview": "Tesla continues to lead the EV market but faces increasing competition in China and Europe. The company is pivoting towards AI and Robotics, with significant investments in FSD and Optimus. Energy Generation and Storage revenue is growing rapidly, diversifying the revenue mix.",
            "corporateCreditRating": {"rating": "A-", "outlook": "Stable", "justification": "Strong balance sheet with significant cash reserves and no net debt. Margins have compressed due to price cuts but remain healthy relative to mass-market peers."},
            "financialPerformance": {"revenue": "96.8B", "adjustedEBITDA": "14.2B", "freeCashFlow": "4.4B", "leverage": "0.1x"},
            "sncfRegulatoryRating": {"indicativeRating": "Pass", "justification": "Financials are robust; no immediate regulatory concerns that threaten solvency."},
            "strengths": ["Brand dominance in EV", "Technology leadership (FSD, Battery)", "Supercharger network", "Strong balance sheet"],
            "weaknesses": ["Key man risk (Elon Musk)", "Margin compression", "Regulatory scrutiny on FSD"],
            "specialFocusAreas": ["FSD rollout and take rate", "Robotaxi platform launch", "Optimus development"]
        }
    else:
        return {
            "reportTitle": f"AI-Generated Corporate Credit Assessment: {company_name} ({ticker})",
            "assessmentDate": "2024-10-28",
            "companyName": company_name,
            "tickerSymbol": ticker,
            "overview": "DraftKings operates as a digital sports entertainment and gaming company. It provides users with daily fantasy sports, sports betting, and iGaming opportunities. The company is focused on acquiring customers efficiently and achieving profitability.",
            "corporateCreditRating": {"rating": "B+", "outlook": "Stable", "justification": "Reflects leading market position and revenue growth, offset by historical losses and competitive pressures."},
            "financialPerformance": {"revenue": "1.2B", "adjustedEBITDA": "95M", "freeCashFlow": "-50M", "leverage": "5.6x"},
            "sncfRegulatoryRating": {"indicativeRating": "Special Mention", "justification": "Due to ongoing losses and high leverage, though liquidity remains adequate."},
            "strengths": ["Strong brand recognition", "Market leadership in OSB and iGaming", "Scalable technology platform"],
            "weaknesses": ["History of net losses", "High marketing and promotional spend", "Intense competition"],
            "specialFocusAreas": ["Path to sustained profitability", "Integration of acquisitions (e.g., Jackpocket)"]
        }

def generate_report(prompt, company_name="DraftKings Inc.", ticker="DKNG"):
    """
    Generates a credit report by calling the OpenAI API.
    If the API key is not available, it returns a mock response.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("\n--- WARNING: OPENAI_API_KEY not found. ---")
        print("Falling back to a mock LLM response. To use a real LLM, please set the OPENAI_API_KEY environment variable.")
        return get_mock_response(company_name, ticker)

    print("\n--- Calling OpenAI API to Generate Report ---")
    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an expert credit analyst. Your task is to generate a corporate credit report in a structured JSON format."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )

        report_str = response.choices[0].message.content
        report_dict = json.loads(report_str)

        print("--- Successfully received and parsed report from OpenAI API. ---")
        return report_dict

    except openai.APIConnectionError as e:
        print(f"OpenAI API Connection Error: {e.__cause__}")
    except openai.RateLimitError as e:
        print(f"OpenAI API Rate Limit Error: {e.response.status_code} {e.response.text}")
    except openai.APIStatusError as e:
        print(f"OpenAI API Status Error: {e.status_code} - {e.response}")
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON from LLM response: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during the LLM call: {e}")

    print("--- LLM call failed. Returning None. ---")
    return None
