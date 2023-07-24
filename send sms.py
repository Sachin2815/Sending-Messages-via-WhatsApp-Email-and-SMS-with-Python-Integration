# Install Twilio library first: pip install twilio
from twilio.rest import Client

# Your Twilio account SID and Auth Token
account_sid = 'ACb9a589d15b3f0bbfb919d52e435105b2'
auth_token = 'a9288749a6614d1e3b17c96d38589e5c'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Replace 'to_phone_number' with the recipient's phone number
# Replace 'from_phone_number' with your Twilio phone number
message = client.messages.create(
    body="Hey,Azfar are you completed your python task",
    from_='+12294584818',  # Replace with your Twilio phone number
    to='+917739318770'      # Replace with the recipient's phone number
)

print("Message sent successfully!")
