import requests
import allure
import pytest

#from conftest import generator
#from conftest import create_user

from data import Endpoints
from data import FakeData

class TestLogin:

    def test_login_under_existing_user_success_login(self, generator):

        url_create_user = Endpoints.CREATE_USER
        email, password, firstName = generator
        data = {

            "email": email,
            "password": password,
            "name": firstName

        }

        response_register = requests.post(url_create_user, data)

        r = response_register.json()
        access_token = r['accessToken']
        print(access_token)

        refresh_token = r['refreshToken']
        print(refresh_token)

        # Проверяем авторизацию:

      #  email, password, firstName = generator

        data_login = {
            "email": email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response_login = requests.post(url_login, data_login, headers={'Authorization': access_token})

        assert response_login.status_code == 200

    def test_login_under_unexisting_user_unable_to_login(self, generator): # тут

        url = Endpoints.CREATE_USER
        email, password, firstName = generator
        data = {

            "email": email,
            "password": password,
            "name": firstName

        }

        response_register = requests.post(url, data)

        r = response_register.json()
        access_token = r['accessToken']
        print(access_token)

        refresh_token = r['refreshToken']
        print(refresh_token)

        # Проверяем авторизацию:

      #  email, password, firstName = generator

        data_login = {
            "email": "this_email_does_not_exist@yandex.jj", # несуществующий email
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response = requests.post(url_login, data_login, headers={'Authorization': access_token})

        assert response.status_code == 401

# ПРОДОЛЖИТЬ ТУТ


