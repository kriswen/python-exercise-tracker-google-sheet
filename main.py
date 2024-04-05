import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
APP_ID = os.environ.get("APP_ID", "app id not exist")
APP_KEY = os.environ.get("APP_KEY", "app key not exist")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "sheety token not exist")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "sheety endpoint url not exist")

WEIGHT = 80
HEIGHT = 170
AGE = 35

# https://docx.syndigo.com/developers/docs/natural-language-for-exercise
nutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5d3870eff07722cc9c22d93d32ff97d4/myWorkouts/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

body = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

# post to nutrition api and get response
response = requests.post(nutritionix_exercise_endpoint, headers=headers, json=body)
response.raise_for_status()
result = response.json()
exercises = result["exercises"]
for exercise in exercises:
    exercise_name = exercise["name"]
    exercise_duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    # print(f"Date:{today_date}\nTime:{today_time}\nExercise name:{exercise_name}\nExercise time:{exercise_duration}\n"
    #       f"Calories Burned:{calories}\n")
    # add row to google sheet - https://sheety.co/docs/requests.html
    # Sheety expects your record to be nested in a singular root property named after your sheet.
    # For example if your endpoint is named emails, nest your record in a property called email.
    # Sheety camelCases all JSON keys, so a header named "First Name" will become "firstName".
    today_date = datetime.now().strftime('%m/%d/%Y')
    today_time = datetime.now().strftime('%X')
    # today_time = datetime.now().strftime('%H:%M:%S %p')
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }
    exercise_param = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": calories,
        }
    }
    # post data to google sheet
    post_response = requests.post(SHEETY_ENDPOINT, json=exercise_param, headers=headers)
    post_response.raise_for_status()
    print(f"Adding {exercise_name} to google sheet, response:{post_response}")
