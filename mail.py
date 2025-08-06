
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import streamlit as st

SENDER_EMAIL = "shivkiranchitkulwar123@gmail.com"

SENDER_APP_PASSWORD = st.secrets["SENDER_APP_PASSWORD"]


EMAIL_SUBJECT = "Software and AI Developer interested in joining your team"

EMAIL_BODY = """
Respected Sir/Madam,

I am writing to express my keen interest in software development opportunities at your company. I have experience in development and enjoy tackling new challenges.

My resume is attached, which outlines my background in more detail. I am available for an interview at your earliest convenience and look forward to hearing from you.

Sincerely,

Shivkiran Santosh Chitkulwar
+91 9921316791
shivkiranchitkulwar123@gmail.com
"""

ATTACHMENT_FILENAME = "resume.pdf"

def send_email(recipient_email):
    """
    Constructs and sends an email using the hardcoded credentials above.
    Returns a tuple (bool, str) indicating success and a message.
    """
    if not os.path.exists(ATTACHMENT_FILENAME):
        return False, f"Error: Attachment file '{ATTACHMENT_FILENAME}' not found."

    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = recipient_email
        msg['Subject'] = EMAIL_SUBJECT
        msg.attach(MIMEText(EMAIL_BODY, 'plain'))

        with open(ATTACHMENT_FILENAME, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {ATTACHMENT_FILENAME}")
        msg.attach(part)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True, "Email sent successfully!"

    except Exception as e:
        return False, f"Failed to send email. Error: {e}"