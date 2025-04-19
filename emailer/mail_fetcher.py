import imaplib
import email
import os

def download_resumes_from_email(email_user, email_pass, output_folder='downloads'):
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_user, email_pass)
    mail.select("inbox")

    result, data = mail.search(None, '(UNSEEN SUBJECT "Resume")')  # or customize

    ids = data[0].split()
    os.makedirs(output_folder, exist_ok=True)

    for email_id in ids:
        result, msg_data = mail.fetch(email_id, "(RFC822)")
        raw_email = msg_data[0][1]
        msg = email.message_from_bytes(raw_email)

        for part in msg.walk():
            if part.get_content_maintype() == "multipart":
                continue
            if part.get("Content-Disposition") is None:
                continue

            filename = part.get_filename()
            if filename and filename.endswith((".pdf", ".docx")):
                filepath = os.path.join(output_folder, filename)
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))
                print(f"Saved: {filepath}")
