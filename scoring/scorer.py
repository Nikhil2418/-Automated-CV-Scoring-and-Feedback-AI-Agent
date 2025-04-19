# cv_scoring_agent/scoring/scorer.py

import re
from config import WEIGHTS, AI_KEYWORDS

def score_resume(text):
    score = {}

    # Experience
    experience_years = len(re.findall(r'\b\d{4}\b', text))
    score['experience'] = min(experience_years / 10, 1.0)

    # Education
    education_keywords = ['bachelor', 'master', 'phd', 'b.tech', 'm.tech', 'degree']
    score['education'] = any(keyword in text.lower() for keyword in education_keywords)
    score['education'] = float(score['education'])

    # Skills
    skill_count = sum(1 for keyword in AI_KEYWORDS if keyword in text.lower())
    score['skills'] = min(skill_count / 10, 1.0)

    # Formatting (just a proxy for now: length of text)
    score['formatting'] = 1.0 if len(text) > 500 else 0.5

    # Keywords
    keyword_presence = any(kw in text.lower() for kw in AI_KEYWORDS)
    score['keywords'] = float(keyword_presence)

    final_score = sum(score[k] * WEIGHTS[k] for k in WEIGHTS)

    return round(final_score * 100, 2), score
