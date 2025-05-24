# Functions to parse input credit reports.
# Extracts relevant sections and content from various report formats (e.g., text, JSON).

import json
import os

def load_ai_report_from_json(filepath: str):
    """
    Loads an AI-generated report from a JSON file.

    Args:
        filepath (str): The full path to the JSON file.

    Returns:
        dict: The loaded report data as a dictionary, or None if an error occurs.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            report_data = json.load(f)
        return report_data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading {filepath}: {e}")
        return None

# Example Usage (typically called from another script like run_credit_judge_poc.py):
# if __name__ == '__main__':
#     # Construct path relative to this script or use absolute paths
#     # This example assumes the script is in src/processing and data is in ../../data/
#     script_dir = os.path.dirname(__file__)
#     example_report_path = os.path.join(script_dir, '..', '..', 'data', 'reports_to_be_judged', 'dkng_ai_report.json')
#     
#     print(f"Attempting to load: {example_report_path}")
#     report = load_ai_report_from_json(example_report_path)
#     
#     if report:
#         print("Report loaded successfully.")
#         # print(f"Report Title: {report.get('reportTitle')}")
#         # print(f"Company Name: {report.get('companyName')}")
#         # print(f"Inferred Rating: {report.get('corporateCreditRating', {}).get('rating')}")
#     else:
#         print("Failed to load report.")
