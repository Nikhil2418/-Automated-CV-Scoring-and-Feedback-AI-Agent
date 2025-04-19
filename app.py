# cv_scoring_agent/app.py

import streamlit as st
import tempfile
from pathlib import Path
from scoring.parser import extract_resume_text
from scoring.scorer import score_resume
from scoring.feedback import generate_feedback
from scoring.matcher import compute_jd_cv_match

# ------------------ PAGE SETUP ------------------
st.set_page_config(page_title="AI Resume Scorer", layout="centered")

# ------------------ STYLES ------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f2f6f9 0%, #e9edf5 100%);
    }
    .title {
        font-size: 2.6em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.2em;
        text-align: center;
        color: #444;
        margin-bottom: 2em;
    }
    .upload-box {
        border: 2px dashed #bbb;
        border-radius: 10px;
        padding: 2em;
        background-color: #f9f9f9;
        text-align: center;
    }
    .score-box {
        background-color: #ffffff;
        border-left: 6px solid #4CAF50;
        padding: 1em 1.5em;
        margin: 1.5em 0;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.06);
    }
    .footer {
        margin-top: 3em;
        text-align: center;
        font-size: 0.95em;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("<div class='title'>📄 Automated CV Scoring and Feedback AI Agent</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Free AI resume scoring and JD matching tool to boost your job chances.</div>", unsafe_allow_html=True)

# ------------------ RESUME UPLOAD ------------------
st.markdown("#### Upload Your Resume (PDF or DOCX)")
with st.container():
    uploaded_file = st.file_uploader("", type=["pdf", "docx"], label_visibility="collapsed")

# ------------------ JOB DESCRIPTION ------------------
st.markdown("#### Paste Job Description (Optional but Recommended)")
job_description = st.text_area("Paste the job description you're targeting", height=200)

# ------------------ PROCESS ------------------
if uploaded_file and job_description.strip():
    suffix = Path(uploaded_file.name).suffix
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        resume_text = extract_resume_text(tmp_path)
        score, breakdown = score_resume(resume_text)
        feedback = generate_feedback(score, breakdown)
        jd_match = compute_jd_cv_match(job_description, resume_text)

        # Scores
        st.markdown(f"<div class='score-box'><b>✅ Resume Score:</b> {score}/100</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='score-box'><b>📊 JD-CV Match Score:</b> {jd_match}%</div>", unsafe_allow_html=True)

        st.markdown("#### 📋 AI-Generated Feedback")
        st.text_area("Feedback", feedback, height=300)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

elif uploaded_file:
    st.info("Please paste a job description above to calculate JD-CV match score.")

# ------------------ FOOTER ------------------
st.markdown("<div class='footer'>Made with ❤️ by <strong>Nikhil Kumar</strong></div>", unsafe_allow_html=True)
