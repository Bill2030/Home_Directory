import requests

prices_url= "https://api.sheety.co/87be0f6bb293d3dc42f43e369a1129a1/copyOfFlightDeals/prices"

response = requests.get(url=prices_url)
print(response.json())["prices"]