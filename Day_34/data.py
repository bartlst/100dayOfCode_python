import requests

PROPERTIES = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php", params=PROPERTIES)
question_data = response.json()['results']
