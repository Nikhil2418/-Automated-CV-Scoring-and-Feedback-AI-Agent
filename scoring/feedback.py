# cv_scoring_agent/scoring/feedback.py

def generate_feedback(score, breakdown):
    feedback = f"Your overall resume score is: {score}/100.\n\n"
    feedback += "Breakdown:\n"
    for section, value in breakdown.items():
        feedback += f"- {section.capitalize()}: {round(value * 100, 2)}%\n"

    # Basic strengths/weaknesses
    strengths = [k for k, v in breakdown.items() if v >= 0.7]
    weaknesses = [k for k, v in breakdown.items() if v < 0.5]

    feedback += "\nStrengths: " + ", ".join(strengths) if strengths else ""
    feedback += "\nAreas to Improve: " + ", ".join(weaknesses) if weaknesses else ""
    return feedback
