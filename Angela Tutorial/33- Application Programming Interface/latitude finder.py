import requests

MY_LAT = -1.292066
MY_LONG = -1.292066


parameters = {
    "lat":MY_LAT,
    "lng":MY_LONG
}
response = requests.get(url="https://api.sunrise-sunset.org/json")
response.raise_for_status()
data = response.json()
print(data)
results = data["results"]["sunset"]
print(results)





