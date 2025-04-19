# cv_scoring_agent/config.py

# Scoring Weights
WEIGHTS = {
    'education': 0.2,
    'experience': 0.3,
    'skills': 0.3,
    'formatting': 0.1,
    'keywords': 0.1,
}

# Keywords to check for AI relevance
AI_KEYWORDS = [
    "machine learning", "deep learning", "AI", "artificial intelligence", "NLP",
    "computer vision", "transformer", "bert", "gpt", "pytorch", "tensorflow", "scikit-learn"
]

# Email Settings (dummy; replace during deployment)
EMAIL_SENDER = "your_email@example.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
