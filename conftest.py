import pytest
import requests
import helpers
from methods.courier_methods import CourierMethods
from urls import Urls


@pytest.fixture()
def courier():
    courier = CourierMethods()
    create_courier = helpers.return_main_login_params()
    response = courier.login_courier(create_courier)
    yield courier
    requests.delete(f'{Urls.BASE_URL}{Urls.COURIER}{response['id']}')

