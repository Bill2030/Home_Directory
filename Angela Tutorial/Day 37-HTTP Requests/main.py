import requests
from datetime import *

USERNAME = "sila"
TOKEN = "YRJTKKKFJTK"


pixela_endpoint = "https://pixe.la/v1/users"
user_params={
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)


#graph_endpoint = f"{pixela_endpoint}/ {USERNAME}/graphs"
graph_endpoint = "https://pixe.la/v1/users/sila/graphs"
graph_config={
    "id":"graph1",
    "name":"cycling graph",
    "unit":"km",
    "type":"float",
    "color":"sora"
}
headers={
   "X-USER-TOKEN":TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_endpoint_creation = "https://pixe.la/v1/users/sila/graphs/graph1"

today = datetime(year=2023, month=5, day=25)
#print(today.strftime("%Y%m%d"))

graph_configuration={
    "date":today.strftime("%Y%m%d"),
    "quantity":"20.5"
}
response = requests.post(url=pixel_endpoint_creation, json=graph_configuration, headers=headers)

#API Put method
update_endPoint = "https://pixe.la/v1/users/sila/graphs/graph1/20230525"


new_pixel_data={
"quantity":"56.2"
}
response = requests.put(url=update_endPoint, json=new_pixel_data, headers=headers)
#print(response.text)

#Delete Requests
delete_endpoint = "https://pixe.la/v1/users/sila/graphs/graph1/20230525"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)






