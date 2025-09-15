# ui.py

import streamlit as st
from mail import send_email, ATTACHMENT_FILENAME

st.set_page_config(page_title="Quick Email Sender", layout="centered")
st.title("🚀 Quick Email Sender")
st.write(f"This app sends a predefined email with the attachment '{ATTACHMENT_FILENAME}'.")
st.write("---")

recipient = st.text_input("Enter the recipient's email address:")

if st.button("Send Email"):
    if not recipient:
        st.warning("Please enter a recipient's email address.")
    else:
        with st.spinner("Sending email..."):
            success, message = send_email(recipient)
        
        if success:
            st.success(message)
        else:
            st.error(message)

st.write("""
# LINKEDIN

https://www.linkedin.com/in/shivkiran-chitkulwar-b84a36273/

I'm Shivkiran, a Full Stack AI Developer with 1+ years of experience, including Gen AI. Actively seeking new opportunities and would be grateful for your referral.I am ready for interview.
         

# WellFound

I'm drawn to this company because of its reputation for innovation and its commitment to employee growth. I am passionate about tackling new challenges and contributing to impactful projects, and I believe the collaborative environment here would be the perfect place for me to apply my skills and continue learning.
""")