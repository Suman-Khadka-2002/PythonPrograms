import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# load from the env variables from file
sender_email = os.environ.get("SENDER_EMAIL")
receiver_email = os.environ.get("RECEIVER_EMAIL")
password = os.environ.get("PASSWORD")

message = MIMEMultipart("alternative")
message["Subject"] = "Subject you want"
message["From"] = sender_email
message["To"] = receiver_email
# create HTML version of your message
text = """ \
Hi, Mr. President
I am Suman"""
html = """
<html>
    <body>
        <p>I am writing this application for the job.<br>
        <a href="https://www.facebook.com">
        </p>
    </body>
</html>
"""
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(user=sender_email, password=password)
    server.sendmail(sender_email, receiver_email, message.as_string())
