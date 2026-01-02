import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

print("HOST:", EMAIL_HOST)
print("PORT:", EMAIL_PORT)

recipients = [
    "kasireddypadma8873@gmail.com",
    "venkatapadmalathakasireddy@gmail.com",
]

message = """Subject: Python Training Notification

Hello,

This is your class friend Padmalatha.

hope this email finds you well.

Regards,
Padmalatha
padmalatha3633@gmail.com
"""

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT, timeout=10)
    server.ehlo()
    server.starttls()
    server.login(EMAIL_USER, EMAIL_PASSWORD)

    for receiver in recipients:
        server.sendmail(
            EMAIL_USER,
            receiver,
            message
        )
        print(f"Email sent successfully to {receiver}")

    server.quit()

except Exception as e:
    print("ERROR:", e)