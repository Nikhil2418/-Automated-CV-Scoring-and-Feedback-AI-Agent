import re

def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'(\+91[\-\s]?)?[0]?(91)?[789]\d{9}', text)
    return match.group(0) if match else "Not found"

def mask_email(email):
    if "@" not in email:
        return "Not found"
    return email[0] + "***@" + email.split("@")[1]

def mask_phone(phone):
    return phone[:2] + "*****" + phone[-3:] if len(phone) >= 10 else "Not found"
