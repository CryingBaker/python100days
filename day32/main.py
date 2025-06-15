import smtplib
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
to_email = os.environ.get("SENDTO")

# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#     connection.starttls()
#     connection.login(user = my_email, password= password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_email,
#                         msg = "Subject: Hi Atharv!\n\nHello")
#     connection.close()

now = dt.datetime.now()
print(now.weekday())

date_of_birth = dt.datetime(2004,11,18,13,30)
print(date_of_birth)