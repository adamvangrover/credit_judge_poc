from textblob import TextBlob
import textstat

def calculate_sentiment(text):
    """
    Calculates polarity and subjectivity using TextBlob.
    Returns a dictionary with 'polarity' and 'subjectivity'.
    """
    if not text:
        return {"polarity": 0, "subjectivity": 0}

    blob = TextBlob(text)
    return {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity
    }

def calculate_readability(text):
    """
    Calculates the Flesch Reading Ease score using textstat.
    Returns the score.
    """
    if not text:
        return 0
    return textstat.flesch_reading_ease(text)

def calculate_keyword_density(text, keywords):
    """
    Calculates the density of specific keywords in the text.
    Returns a dictionary mapping keywords to their count per 1000 words.
    """
    if not text:
        return {k: 0 for k in keywords}

    text_lower = text.lower()
    words = text_lower.split()
    total_words = len(words)
    if total_words == 0:
        return {k: 0 for k in keywords}

    density = {}
    for keyword in keywords:
        count = text_lower.count(keyword.lower())
        density[keyword] = (count / total_words) * 1000

    return density

def calculate_numerical_density(text):
    """
    Calculates the density of numerical figures in the text.
    Returns the count of numbers per 1000 words.
    """
    if not text:
        return 0

    words = text.split()
    total_words = len(words)
    if total_words == 0:
        return 0

    num_count = sum(1 for word in words if any(char.isdigit() for char in word))
    return (num_count / total_words) * 1000

def analyze_report_content(report_data):
    """
    Aggregates all quantitative metrics for a given report data dictionary.
    Assumes report_data contains standard sections.
    """
    # Combine relevant text sections for analysis
    text_sections = []

    if "overview" in report_data:
        text_sections.append(report_data["overview"])
    if "corporateCreditRating" in report_data and isinstance(report_data["corporateCreditRating"], dict):
        text_sections.append(report_data["corporateCreditRating"].get("justification", ""))
    if "sncfRegulatoryRating" in report_data and isinstance(report_data["sncfRegulatoryRating"], dict):
        text_sections.append(report_data["sncfRegulatoryRating"].get("justification", ""))

    # Flatten lists (strengths, weaknesses, etc.)
    for key in ["strengths", "weaknesses", "specialFocusAreas"]:
        if key in report_data and isinstance(report_data[key], list):
             text_sections.extend(report_data[key])

    full_text = " ".join(text_sections)

    sentiment = calculate_sentiment(full_text)
    readability = calculate_readability(full_text)

    risk_keywords = ["risk", "loss", "decline", "debt", "uncertainty", "challenge", "burn"]
    keyword_density = calculate_keyword_density(full_text, risk_keywords)

    numerical_density = calculate_numerical_density(full_text)

    return {
        "sentiment": sentiment,
        "readability": readability,
        "keyword_density": keyword_density,
        "numerical_density": numerical_density,
        "full_text_length": len(full_text)
    }
