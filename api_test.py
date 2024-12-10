# Иващенко Полина, 24-я когорта — Финальный проект. Инженер по тестированию плюс
from sender_stand_request import get_track, get_order_by_track


def test_get_order_by_track():
    track = get_track()
    order_response = get_order_by_track(track)
    status_code = order_response.status_code
    assert status_code == 200


test_get_order_by_track()
