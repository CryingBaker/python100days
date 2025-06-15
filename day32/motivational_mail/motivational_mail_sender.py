import datetime as dt
import smtplib
import dotenv
import random
import os

dotenv.load_dotenv("../.env")

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
to_email = os.environ.get("SENDTO")

def choose_quote():
    with open("quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        return random.choice(quotes)

now = dt.datetime.now()

if now.weekday() == 6:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg = f"Subject: Monday Motivation!\n\n{choose_quote()}".encode("utf-8"))

