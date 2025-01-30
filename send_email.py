import smtplib
import json

# Load the config file
with open('config.json', "r") as file:
    config = json.load(file)

def send_email(sender_email, receiver_email, subject, email_content):
    """
    Sends an email with the AI-generated content.

    Args:
        sender_email (str): Sender's email.
        receiver_email (str): Receiver's email.
        subject (str): Email subject.
        email_content (str): Email body content.
    """
    try:
        # Use an App Password instead of a normal password
        app_password = config.get("app_password") #"kngf bsbb mhhe brns"  

        # Set up SMTP server
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, app_password)

        # Format email subject and body
        email_message = f"Subject: {subject}\n\n{email_content}"

        # Send email
        server.sendmail(sender_email, receiver_email, email_message)
        server.quit()
        print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
