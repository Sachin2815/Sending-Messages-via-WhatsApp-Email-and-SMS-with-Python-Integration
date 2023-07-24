import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Set up the SMTP server
        smtp_server = "smtp.gmail.com"
        port = 587  # Use 465 for SSL or 587 for TLS
        smtp = smtplib.SMTP(smtp_server, port)
        smtp.starttls()  # Encrypt the connection

        # Login to your email account
        smtp.login(sender_email, sender_password)

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach the body to the email
        message.attach(MIMEText(body, "plain"))

        # Send the email
        smtp.sendmail(sender_email, receiver_email, message.as_string())

        # Quit the SMTP server
        smtp.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Replace these with your actual email credentials and email content
    sender_email = "sachinsingh58624@gmail.com"
    sender_password = "password"
    receiver_email = "mayank07082001@gmail.com"
    subject = "Test Email from Python"
    body = "This is a test email sent from Python."

    send_email(sender_email, sender_password, receiver_email, subject, body)
