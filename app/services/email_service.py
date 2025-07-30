import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import settings

# Function to send email using Gmail SMTP
def send_email(to_email: str, subject: str, body: str, html: bool = False):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = settings.sender_email
        msg["To"] = to_email

        # Attach body as plain text or HTML
        mime_body = MIMEText(body, "html" if html else "plain")
        msg.attach(mime_body)

        # Connect to Gmail SMTP server
        with smtplib.SMTP(settings.smtp_server, settings.smtp_port) as server:
            server.starttls()
            server.login(settings.sender_email, settings.sender_password)
            server.sendmail(settings.sender_email, to_email, msg.as_string())

        print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")