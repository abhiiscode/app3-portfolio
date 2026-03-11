import smtplib, ssl
import os

def send_email_fung(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = "pythonwithabhi@gmail.com"
    password = os.getenv("PASSWORD_for_app3")
    receiver = "abktpass@gmail.com"
    my_context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)