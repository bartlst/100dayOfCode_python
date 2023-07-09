import requests
import datetime

USER_TOKEN = "vFrrq-IEcqtrCjcHJ4FuelSWpdfS$l"
USERNAME = "bartlst"
BOOK_GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{BOOK_GRAPH_ID}"


USER_PARAMS = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

HEADERS = {
    "X-USER-TOKEN": USER_TOKEN
}

GRAPH_PARAMS = {
    "id": BOOK_GRAPH_ID,
    "name": "Book reading graph",
    "unit": "Page",
    "type": "int",
    "color": "ajisai"
}

PIXEL_PARAMS = {
    "date": None,
    "quantity": None,
    "optionalData": ""
}

NEW_PIXEL_PARAMS = {
    "quantity": "55"
}

# Creating a user account
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

# Creating a graph
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_PARAMS, headers=HEADERS)
# print(response.text)

# Posting a pixel to a graph
today = datetime.datetime.now().date()
PIXEL_PARAMS["date"] = today.strftime("%Y%m%d")
PIXEL_PARAMS["quantity"] = "1"

# post pixel request

# print(PIXEL_PARAMS)
response = requests.post(url=POST_PIXEL_ENDPOINT, json=PIXEL_PARAMS, headers=HEADERS)
print(response.text)

# put pixel request

UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{BOOK_GRAPH_ID}/{PIXEL_PARAMS['date']}"

response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=NEW_PIXEL_PARAMS, headers=HEADERS)
print(response.text)

# delete pixel request
response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=HEADERS)
print(response.text)