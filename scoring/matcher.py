# cv_scoring_agent/scoring/matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_jd_cv_match(jd_text, cv_text):
    """
    Compare job description and resume text using cosine similarity of TF-IDF vectors.
    Returns a percentage score.
    """
    documents = [jd_text, cv_text]
    vectorizer = TfidfVectorizer().fit_transform(documents)
    similarity_matrix = cosine_similarity(vectorizer)
    similarity_score = similarity_matrix[0, 1]  # JD vs CV
    return round(similarity_score * 100, 2)
