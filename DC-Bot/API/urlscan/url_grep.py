import requests
import json

from API.config import URLSCAN_TOKEN as TOKEN


def urlscan(requesturl):
    headers = {'API-Key': TOKEN, 'Content-Type': 'application/json'}
    data = {"url": requesturl, "visibility": "public"}
    response = requests.post('https://urlscan.io/api/v1/scan/', headers=headers, data=json.dumps(data))

    return response
