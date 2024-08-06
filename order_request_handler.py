import app_configuration
import requests
import test_data


def post_create_order(body):
    return requests.post(app_configuration.URL_SERVICE + app_configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=test_data.headers)


def get_order_by_track(track):
    return requests.get(app_configuration.URL_SERVICE + app_configuration.GET_ORDER_BY_TRACK_PATH + "?t=" + str(track))




