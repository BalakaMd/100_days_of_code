import random
import smtplib
import datetime as dt
from random import choice
import pandas as pd

now = (dt.datetime.now().day, dt.datetime.now().month)
# 1. Update the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row['day'], data_row['month']) for (index, data_row) in data.iterrows()}
# 2. Check if today matches a birthday in the birthdays.csv
if now in birthdays_dict:
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
# 4. Send the letter generated in step 3 to that person's email address.

