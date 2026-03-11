import streamlit as sl
from send_email import send_email_fung
import pandas

sl.set_page_config("wide")

sl.header("For More Information CONTACT Us!")

df = pandas.read_csv("topics.csv")

with sl.form(key="email_form"):
    user_email = sl.text_input("Enter your email")
    option = sl.selectbox(
        "How would you like to be contacted?",
        df["topic"])
    user_row_message = sl.text_area("Enter your message")
#1    user_row_message = user_row_message + "\n" + user_email
    #for f"" \ is very imp

    user_message = f"""\
Subject: New Email from {user_email}

From: {user_email}
topic: {option} 
{user_row_message}
"""
    # '''it will send sender email address'''
    button = sl.form_submit_button("Submit")
    if button:
        send_email_fung(user_message)  #fist
        sl.info("Your Email Was Send Sucessfully!")
