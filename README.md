# Exercise Tracker

## Introduction
This project is an exercise tracker that allows users to input their exercises and track their workouts. It utilizes the Nutritionix API to obtain exercise data based on user input and then logs the workout details to a Google Sheet using the Sheety API.

## Requirements
- Python 3
- `requests` library (install via `pip install requests`)
- `dotenv` library (install via `pip install python-dotenv`)

## Installation
1. Clone the repository:
````
git clone <repository_url>
cd exercise-tracker
````

2. Create a `.env` file in the root directory and add your API keys:
````
APP_ID=your_nutritionix_app_id
APP_KEY=your_nutritionix_app_key
SHEETY_TOKEN=your_sheety_token
SHEETY_ENDPOINT=our_sheety_url
````
3. Run the script:
````
python main.py
````

4. Follow the prompts to input your exercises.

## Features
- Input exercises using natural language.
- Automatically calculates calories burned based on exercise type, duration, weight, height, and age.
- Logs exercise details to a Google Sheet for tracking and analysis.

## Usage
1. Run the script and follow the prompts to input your exercises.
2. The script will post the exercise data to the Nutritionix API and retrieve exercise details.
3. Exercise details (including date, time, exercise name, duration, and calories burned) will be logged to a Google Sheet.

## Dependencies
- [Python](https://www.python.org/)
- [requests](https://docs.python-requests.org/en/master/)
- [dotenv](https://pypi.org/project/python-dotenv/)
