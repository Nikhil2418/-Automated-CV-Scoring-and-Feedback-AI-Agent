def send_feedback_email(to_email, score, jd_match, feedback):
    subject = "Your Resume Score and Feedback"
    body = f"""
Hi,

Thank you for submitting your resume.

Here is your feedback:

✅ Resume Score: {score}/100  
📊 JD-CV Match: {jd_match}%  
📝 Feedback:  
{feedback}

Best of luck,
AI Resume Bot
"""
    # Use smtplib to send this
