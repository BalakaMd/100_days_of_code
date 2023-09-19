from datetime import datetime
import requests
import os

APP_ID = os.environ['NUTRITIONIX_APP_ID']
API_KEY = os.environ["NUTRITIONIX_API"]
NUTRITIONIX_HEADERS = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}
SHEETY_HEADERS = {
    'Authorization': f'Basic {os.environ["SHEETY_TOKEN"]}'
}
DATE_NOW = datetime.now().date().strftime('%d/%m/%Y')
TIME_NOW = datetime.now().time().strftime("%H:%M")

nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("Tell us about your training: ")

nutritionix_post_request_body = {
    "query": f"{exercise}",
    "gender": "male",
    "weight_kg": 76.5,
    "height_cm": 181.00,
    "age": 28
}

nutritionix_response = requests.post(url=nutritionix_exercise_endpoint, json=nutritionix_post_request_body,
                                     headers=NUTRITIONIX_HEADERS)
nutritionix_response.raise_for_status()

results = nutritionix_response.json()['exercises']

for result in results:
    exercise = result['name'].capitalize()
    duration = result['duration_min']
    calories = result['nf_calories']
    distance = result['met']

    shetee_post_endpoint = 'https://api.sheety.co/56967c3701d5f22d04594e57bb8b8627/myWorkouts/workouts'
    shetee_post_request_body = {'workout': {
        'date': f'{DATE_NOW}',
        'time': f'{TIME_NOW}',
        'exercise': exercise,
        'duration': duration,
        'calories': calories,
        'distance': f'{distance}km',
    }
    }
    sheety_response = requests.post(url=shetee_post_endpoint,
                                    json=shetee_post_request_body,
                                    headers=SHEETY_HEADERS)
    sheety_response.raise_for_status()
print('Thank you very much for your attention ❤️')
