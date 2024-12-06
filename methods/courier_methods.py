import requests
import data
from methods.order_methods import OrderMethods
from urls import Urls


class CourierMethods(OrderMethods):

    def create_courier(self, data_courier):
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', data=data_courier)
        return response.status_code, response.json()

    def login_courier(self, login_courier):
        response = requests.post(f'{Urls.BASE_URL}{Urls.LOGIN_COURIER}', data=login_courier)
        return response.json()

    def create_regular_courier(self):
        static_courier = data.static_courier
        response = requests.post(f'{Urls.BASE_URL}{Urls.COURIER}', data=static_courier)
        return response.status_code, response.json()
