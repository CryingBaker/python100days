import datetime as dt
import os
import smtplib
import pandas
import random
from dotenv import load_dotenv

load_dotenv("../.env")

my_email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")

def send_mail(letter_format, who_to_wish, email_id):
    with open(letter_format) as letter_format_chosen:
        letter_to_send = letter_format_chosen.read()
        letter_to_send = letter_to_send.replace("[NAME]",who_to_wish)
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user = my_email, password= password)
        connection.sendmail(from_addr= my_email, to_addrs= email_id, msg = f"Subject: Birthday Wishes\n\n {letter_to_send}")

birthday_file = pandas.read_csv("birthdays.csv")
birthdays = birthday_file.to_dict(orient="records")
letter_formats = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
now = dt.datetime.now() 

for birthday in birthdays:
    if birthday["month"] == now.month and birthday["day"] == now.day:
        letter_format = random.choice(letter_formats)
        send_mail(letter_format, birthday["name"],birthday["email"])

