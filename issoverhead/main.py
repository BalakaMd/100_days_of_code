import requests
import smtplib
import time
from datetime import datetime

email = "md.balaka@gmail.com"
password = "nwyczmmjzwkyqkyr"

MY_LAT = 32.821150
MY_LONG = 34.969876

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])
print(iss_longitude)
print(iss_longitude)


def check_iss_position():
    """Check position ISS """
    # My position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 \
            and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    """Check Times of Day """
    if sunset < time_now.hour < sunrise:
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    time.sleep(60)
    if is_dark() and check_iss_position():
        subject = 'Subject: Look up !!\n\n '
        massage = f"{subject} It seems the ISS is flying over you look up "

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email,
                                to_addrs=email,
                                msg=massage)
