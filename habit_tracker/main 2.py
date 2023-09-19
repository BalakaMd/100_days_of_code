import requests

PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
USERNAME = "dimka"
TOKEN = "sh$C9DHhmU$rN1"

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=PIXELA_ENDPOINT, json=parameters)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
headers = {
    'X-USER-TOKEN': TOKEN,
}
graph_parameters = {
    'id': 'graph001',
    'name': 'My Coding',
    'unit': 'Hour',
    'type': 'float',
    'color': 'shibafu',
}

post_pixel_endpoint = f"{graph_endpoint}/graph001"
pixel_parameters = {
    'date': '20230904',
    'quantity': '2',
}
response = requests.post(url=post_pixel_endpoint, json=pixel_parameters, headers=headers)
response.raise_for_status()
