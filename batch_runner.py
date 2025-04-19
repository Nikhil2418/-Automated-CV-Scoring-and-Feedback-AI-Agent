import os
from scoring.parser import extract_resume_text
from scoring.scorer import score_resume
from scoring.feedback import generate_feedback
from scoring.matcher import compute_jd_cv_match
from emailer.send_email import send_feedback_email
from utils.helper import extract_email, extract_phone, mask_email, mask_phone

# You can load this dynamically too
JD_TEXT = """Paste the job description text here"""

DOWNLOAD_FOLDER = "downloads"

for file in os.listdir(DOWNLOAD_FOLDER):
    if file.endswith(".pdf") or file.endswith(".docx"):
        filepath = os.path.join(DOWNLOAD_FOLDER, file)
        print(f"Processing {file}...")

        # 1. Extract resume text
        text = extract_resume_text(filepath)

        # 2. Extract personal details
        email_raw = extract_email(text)
        phone_raw = extract_phone(text)
        email_masked = mask_email(email_raw)
        phone_masked = mask_phone(phone_raw)

        # 3. Score and feedback
        score, breakdown = score_resume(text)
        feedback = generate_feedback(score, breakdown)
        jd_match = compute_jd_cv_match(JD_TEXT, text)

        # 4. Send feedback email
        send_feedback_email(email_raw, score, jd_match, feedback, name="Candidate")

        print(f"✅ Feedback sent to {email_raw}")
