import streamlit as sl
from send_email import send_email

sl.header("Contact Me")

with sl.form(key="email_forms"):
    user_email = sl.text_input("Your email address")
    message = sl.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{message}
"""
    button = sl.form_submit_button("Submit")
    print(button)
    if(button):
        send_email(message)
        sl.info("Your email was successfully sent")