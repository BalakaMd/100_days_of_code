import smtplib
import datetime as dt
from random import choice

email = "md.balaka@gmail.com"
password = "nwyczmmjzwkyqkyr"

with open("quotes.txt") as file:
    all_quotes = file.readlines()
    quote = choice(all_quotes)
date = dt.datetime.now()
if date.weekday() == 0:
    massage = f"Subject: Motivational Monday with love <3!\n\n {quote} "

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs="balakinamd@gmail.com",
                            msg=massage)
