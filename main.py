import os

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()

MY_ADDRESS = os.getenv("MY_ADDRESS")
PASSWORD = os.getenv("PASSWORD")
print(MY_ADDRESS)


RECEIVER = os.getenv("RECEIVER")


s = smtplib.SMTP(host="smtp.gmail.com", port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


msg = MIMEMultipart()

msg['From'] = MY_ADDRESS
msg['To'] = RECEIVER
msg['Subject'] = "SMTP message"

message = "hello, this is a message"

msg.attach(MIMEText(message, 'plain'))

s.send_message(msg)
