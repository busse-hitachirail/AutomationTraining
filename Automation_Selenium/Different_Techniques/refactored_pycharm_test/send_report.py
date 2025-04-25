import smtplib
import ssl
import yaml
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

sender = os.getenv("EMAIL_SENDER", config["email"]["sender"])
password = os.getenv("EMAIL_PASSWORD", config["email"]["password"])
recipients = config["email"]["recipients"]

def send_email_report():
    subject = "Selenium Test Report"
    body = "Attached is the latest HTML test report from Selenium automation."
    report_path = "report.html"

    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg["Subject"] = subject
    msg.set_content(body)

    # Attach HTML report
    with open(report_path, "rb") as f:
        report_data = f.read()
        msg.add_attachment(report_data, maintype="text", subtype="html", filename="report.html")

    # Send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.send_message(msg)

    print("Email sent successfully to:", ", ".join(recipients))

if __name__ == "__main__":
    send_email_report()
