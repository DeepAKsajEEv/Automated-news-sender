import smtplib
from main import sms_link, sms_text 
from sms import date


#use username and password of respective user
#use senders and receivers email id's
if date == "08:00 AM":
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user="USER_MAIL_ID", password="USER_PASSWORD")
    connection.sendmail(from_addr="sender@gmail.com",
                        to_addrs="receiver@gmail.com",
                        msg=f"{sms_text}\n\n{sms_link}")

