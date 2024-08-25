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

    # Проверяем авторизацию:

    data_login = {
        "email": email,
        "password": password
    }

    url_login = Endpoints.LOGIN_USER
    requests.post(url_login, data_login, headers={'Authorization': access_token})

    yield access_token

  #  url_delete = Endpoints.DELETE_USER
  #  requests.delete(url_delete, headers={'Authorization': access_token})



@pytest.fixture()
def create_user(generator):

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

    return access_token



