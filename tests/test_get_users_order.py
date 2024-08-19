import requests
import allure
import pytest

from data import Endpoints
from data import FakeData


class TestGetOrders:

    def test_get_orders_authorized_success(self, generator):

        # Создаем пользователя

        url_create_user = Endpoints.CREATE_USER
        email, password, firstName = generator
        data = {

            "email": email,
            "password": password,
            "name": firstName

        }

        response_register = requests.post(url_create_user, data)
        r = response_register.json()
        print(r)

        # Получаем токен

        r = response_register.json()
        access_token = r['accessToken']
        print(access_token)

        # Выполняем авторизацию

        data_login = {
            "email": email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response_login = requests.post(url_login, data_login, headers={'Authorization': access_token})

        print(response_login.status_code)

        # Передаем токен пользователя, получаем список заказов

        url_get_users_orders = Endpoints.GET_ORDERS_OF_CURRENT_USER
        response_get_orders = requests.get(url_get_users_orders, headers={'Authorization': access_token})
        print(response_get_orders.json())
        print(response_get_orders.status_code)

        assert response_get_orders.status_code == 200

    def test_get_orders_unauthorized_success(self, generator):

        url_get_users_orders = Endpoints.GET_ORDERS_OF_CURRENT_USER
        response = requests.get(url_get_users_orders)

        print(response.status_code)
        print(response.json())
        print(response.json()['message'])

        assert response.status_code == 401
        assert response.reason == 'Unauthorized'
        assert response.json()['message'] == 'You should be authorised'


