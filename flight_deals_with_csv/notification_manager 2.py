import pandas as pd
import smtplib


def get_user_data_from_csv():
    with open('users_data.csv') as file:
        new_data = pd.DataFrame(pd.read_csv(file))
        return new_data


user_data = get_user_data_from_csv()
email = "md.balaka@gmail.com"
password = "nwyczmmjzwkyqkyr"


class NotificationManager:
    def __init__(self):
        self.subject = "Subject: Hot price to your flight search!\n\n"

    def send_message(self, new_price, old_price, utc_arrival, airlines, bags_price, city):
        for index, row in user_data.iterrows():
            full_name = row['First Name'] + row['Last Name']
            user_email = row['Email']
            massage = f"Hi Dear {full_name}!\n" \
                      f"We have new hot price to your search.\n" \
                      f"Flight on the {utc_arrival} only {new_price}" \
                      f" euro instead of {old_price} from Tel-Aviv to {city}\n" \
                      f"Airlines : {airlines}, Luggage price: {bags_price}\n" \
                      f"Thank you for using our service!"
            full_massage = f"{self.subject}{massage}"
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(from_addr=email,
                                    to_addrs=user_email,
                                    msg=full_massage)
