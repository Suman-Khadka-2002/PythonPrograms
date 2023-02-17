import smtplib, ssl
import os

port = os.environ.get("PORT")
smtp_server = "smtp.gmail.com"
# load from teh env variable
sender_email = os.environ.get("SENDER_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = input("Enter your password")
message = "Your message here"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(
    host=os.environ.get("HOST"), port=port, context=context
) as server:
    server.login(os.environ.get("SENDER"))
    server.sendmail(sender_email, receiver_email, message)
