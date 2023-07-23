#1. Importing the necessary libraries:
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#2. Defining the send_email function:
def send_email(sender_email, sender_password, receiver_email, subject, message):
    # 3. Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = receiver_email
    email_message['Subject'] = subject


    # 4. Add body to the email
    email_message.attach(MIMEText(message, 'plain'))


    # 5. Create SMTP session for sending the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)

    # Convert the multipart message to a string
    email_text = email_message.as_string()


    # Send the email
    smtp_server.sendmail(sender_email, receiver_email, email_text)
    smtp_server.quit()

# Example usage
sender_email = 'sachinsingh58624@gmail.com'
sender_password = 'passwd'
receiver_email = 'linuxworld.certificates@gmail.com'
subject = 'Hello from sachin!'
message = "I hope you are well , Lets meet soon ."

