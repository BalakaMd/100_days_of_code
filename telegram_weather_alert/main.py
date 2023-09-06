import requests
import telegram
import tracemalloc

tracemalloc.start()

OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/weather'
API_KEY = "3540ae1bd61cfadb79af522f80268a32"
MY_LAT = 32.821150
MY_LONG = 34.969876
TG_TOKEN = "6569854472:AAG31TlvIp4CxAG2yWDf281g2qzkF4cbO74"
CHATS_ID = [328192793, 311711609]

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(OWN_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# Weather parameters
weather_main = weather_data['weather'][0]['main']
weather_description = weather_data['weather'][0]['description'].capitalize()

current_temp = weather_data['main']['temp']
feels_like = weather_data['main']['feels_like']
max_temp = weather_data['main']['temp_max']
min_temp = weather_data['main']['temp_min']

humidity = weather_data['main']['humidity']

# bot = telegram.Bot(token=TG_TOKEN)
# message_text = "Good morning!\n" \
#                f"Today it is going to be {weather_main} in Haifa.\n" \
#                f"{weather_description} is expected.\n\n" \
#                f"Current temperature is {current_temp}.\n" \
#                f"The maximum today is {max_temp} and minimum is {min_temp}. Humidity is {humidity}.\n\n" \
#                f"Have a nice day!"
# url = f'https://api.telegram.org/bot{TG_TOKEN}/sendMessage'
# for user in CHATS_ID:
#     data = {'chat_id': user, 'text': message_text}
#
#     response = requests.post(url, data=data)
