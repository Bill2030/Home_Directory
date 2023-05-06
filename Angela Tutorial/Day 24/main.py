import requests

rel = requests.get("https://www.google.com")
print(rel.content, end='')
#r = requests.get("https://api.github.com/events", stream=True)
#print(r.raw)






























