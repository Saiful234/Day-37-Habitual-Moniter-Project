import requests
from datetime import datetime


USERNAME = "saifr"
TOKEN = "nodsifjdmverdveasy"
GRAPHID = "graph1"

# To Create a new user account
pixela_endpoint = "https://pixe.la/v1/users"

user_parameter = {
    "token": TOKEN,
    "username": "saifr",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_parameter)
print(response.text)

# To Create a new Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hrs",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

# To give a data into the graph
pixel_input_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

today = datetime.today()
today_date = today.strftime("%Y%m%d")
graph_input = {
    "date": today_date,
    "quantity": "10.0",
}

# response = requests.post(url=pixel_input_endpoint, json=graph_input, headers=headers)
# print(response.text)

# To update the value in the graph
update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_date}"

update_input = {
    "quantity": "7.5"
}
# response = requests.put(update_pixel_endpoint, json=update_input, headers=headers)
# print(response.text)


# To delete the data in the graph
delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today_date}"

# response = requests.delete(url= delete_pixel_endpoint, headers=headers)
# print(response.text)