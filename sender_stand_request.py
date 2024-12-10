import requests
from data import TEST_DATA
from configuration import SERVER_URL


def get_track():
    response = requests.post(f"{SERVER_URL}/api/v1/orders", json=TEST_DATA)
    response_json = response.json()
    track = response_json["track"]
    return track


def get_order_by_track(track):
    return requests.get(f"{SERVER_URL}/v1/orders/track?t={track}")