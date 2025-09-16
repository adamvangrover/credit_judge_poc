# Utility functions for parsing and loading credit reports.
import json

def load_ai_report_from_json(filepath):
    """
    Loads a structured AI-generated report from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict: The loaded report data as a dictionary, or None if an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            report_data = json.load(f)
        return report_data
    except FileNotFoundError:
        print(f"Error: Report file not found at {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from {filepath}: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while loading {filepath}: {e}")
        return None

def parse_simulated_rag_report(filepath):
    """
    Loads and 'parses' a plain text file meant to simulate
    retrieved context for a RAG model. For this PoC, it just reads the content.

    Args:
        filepath (str): The path to the text file.

    Returns:
        str: The content of the file, or None if an error occurs.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            report_content = f.read()
        return report_content
    except FileNotFoundError:
        print(f"Error: Simulated report file not found at {filepath}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading {filepath}: {e}")
        return None
