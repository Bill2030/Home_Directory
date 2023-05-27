import requests

API_KEY = "6becdb38d62b3e2237f528b6b3b3ced6"
APP_ID = "8c003a8f"

GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 53
AGE = 40


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)