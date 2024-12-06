import requests
from urls import Urls


class OrderMethods:

    def create_order(self, data_order):
        response = requests.post(f'{Urls.BASE_URL}{Urls.ORDER}', data=data_order)
        return response.json()

    def get_order_list(self):
        response = requests.get(f'{Urls.BASE_URL}{Urls.ORDER}')
        return response.json()
