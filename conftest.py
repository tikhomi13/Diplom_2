import pytest
import allure
import json
from data import FakeData
import requests
import random
import string

from data import FakeData, Endpoints


@pytest.fixture
def generator():

    email, password, firstName = FakeData.get_sign_up_data()  # генерация данных
    return email, password, firstName


@pytest.fixture
def create_user_and_login(generator):

    url = Endpoints.CREATE_USER
    email, password, firstName = generator
    data = {

        "email": email,
        "password": password,
        "name": firstName

    }

    response = requests.post(url, data)

    r = response.json()
    access_token = r['accessToken']
    print(access_token)

    refresh_token = r['refreshToken']
    print(refresh_token)

    # Проверяем авторизацию:

    email, password, firstName = generator

    data_login = {
        "email": email,
        "password": password
    }

    url_login = Endpoints.LOGIN_USER
    response = requests.post(url_login, data_login, headers={'Authorization': access_token})
    return response




