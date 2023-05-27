import requests
import os

My_api = "ZsAbHqg99qOE9aEnHsMqsAK1UQHyHG1Q"

MY_URL = "https://v2.jokeapi.dev/joke/Any?amount=4"

response = requests.get(url=MY_URL)
print(response.raise_for_status())
data = response.json()
print(data)


