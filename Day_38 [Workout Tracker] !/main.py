import requests
import datetime


class Exercise:
    def __init__(self, date, time, exercise, duration, calories):
        self.date = date
        self.time = time
        self.exercise = exercise
        self.duration = duration
        self.calories = calories

    def get_dict(self):
        return{
            "workout":
                {
                    "date": self.date,
                    "time": self.time,
                    "exercise": self.exercise,
                    "duration": self.duration,
                    "calories": self.calories
                }
        }

    def save_into_sheet(self):
        requests.post(url=GOOGLE_SHEET_ENDPOINT, json=self.get_dict(), headers=GOOGLE_SHEET_HEADER)


APP_ID = ""
API_KEY = ""

GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/zxczxczxc/pythonMyWorkouts/workouts"

API_HEADER = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

POST_BODY = {
 "query": "ran 3 miles",
 "gender": "male",
 "weight_kg": 86.5,
 "height_cm": 189.5,
 "age": 23
}

GOOGLE_SHEET_HEADER = {
    "Authorization": "Bearer xxxxxxx"
}


while True:
    now = datetime.datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    exercise = input("exercise: ")
    duration = input("duration: ")
    calories = input("calories: ")
    workout = Exercise(date, time, exercise, duration, calories)
    workout.save_into_sheet()


