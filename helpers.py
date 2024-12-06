import requests
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def return_main_registr_params():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

def return_main_login_params():
    generate = return_main_registr_params()
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=generate)
    if response.status_code == 201:
        return generate
