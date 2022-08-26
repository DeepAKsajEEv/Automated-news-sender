from main import sms_link, sms_text
import os
from twilio.rest import Client
import datetime


account_sid = "YOUR ACCOUNT SID"
auth_token = os.environ.get("AUTH_TOKEN")

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

#sending message at morning 8 am (if condition needed)
date = (datetime.datetime.utcnow()+datetime.timedelta(hours=5, minutes=30)).strftime('%H:%M %p')
if date == "08:00 AM":
  # Find your number used in creating account in twilio.com 
  # and enter number of receiver of message
  message = client.messages.create(
                                body=(f"{sms_text}\n{sms_link}"),
                                from_='FROM_NUMBER',
                                to='TO_NUMBER'
                            )
  
  print(message.sid)


