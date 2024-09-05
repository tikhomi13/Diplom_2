import pytest
from helpers import FakeData
import requests
from data import Endpoints


@pytest.fixture
def generator():

    email, password, firstName = FakeData.get_sign_up_data()

    payload = {

        "email": email,
        "password": password,
        "name": firstName

    }

    return payload


@pytest.fixture(scope='function')
def create_user_and_login(generator):

    url = Endpoints.CREATE_USER
    data = generator
    response = requests.post(url, data)

    r = response.json()
    access_token = r['accessToken']

    my_email = data["email"]
    my_password = data["password"]

    data_login = {
        "email": my_email,
        "password": my_password
    }

    url_login = Endpoints.LOGIN_USER
    requests.post(url_login, data_login, headers={'Authorization': access_token})

    yield access_token

    url_delete = Endpoints.DELETE_USER
    requests.delete(url_delete, headers={'Authorization': access_token})


@pytest.fixture()
def create_user(generator):

    url = Endpoints.CREATE_USER
    data = generator
    response_register = requests.post(url, data)

    r = response_register.json()
    access_token = r['accessToken']

    return access_token
