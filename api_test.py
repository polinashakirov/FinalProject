import requests

SERVER_URL = 'https://590a62da-12d2-464d-8f74-dae9debb27a3.serverhub.praktikum-services.ru'


def get_track():
    response = requests.post(f"{SERVER_URL}/api/v1/orders", json={
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-07",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    })
    response_json = response.json()
    track = response_json["track"]
    return track


def get_order_by_track(track):
    return requests.get(f"{SERVER_URL}/v1/orders/track?t={track}")


def test_get_order_by_track():
    track = get_track()
    order_response = get_order_by_track(track)
    status_code = order_response.status_code
    assert status_code == 200
