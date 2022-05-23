import smtplib
import os

MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")

s = smtplib.SMTP(host='localhost', port=80)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
