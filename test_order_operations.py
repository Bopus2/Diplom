import order_request_handler

import test_data


def create_order():
    response = order_request_handler.post_create_order(test_data.order_body)
    return response.json()["track"]


def test_create_order():
    response = order_request_handler.post_create_order(test_data.order_body)
    assert response.status_code == 201
    assert response.json()["track"] > 0


def test_get_order():
    track = create_order()
    response = order_request_handler.get_order_by_track(track)

    assert response.status_code == 200
    assert response.json()["order"]["track"] == track
