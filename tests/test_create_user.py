import requests
import allure
from conftest import generator
from data import Endpoints
from data import TestData


class TestCreateUser:

    @allure.title("Проверка создания пользователя")
    def test_able_to_create_user_create_user_success(self, generator):

        email, password, firstName = generator
        url = Endpoints.CREATE_USER
        data = {

         "email": email,
         "password": password,
         "name": firstName

        }

        response = requests.post(url, data)
        user_data = list(response.json().values())[1]

        assert 200 == response.status_code
        assert email in list(user_data.values())

    @allure.title("Проверка невозможности создания 2-х пользователей с одним email")
    def test_unable_to_create_user_which_is_already_registered_response_403(self):

        url = Endpoints.CREATE_USER
        data = {

         "email": TestData.email_that_already_exists,
         "password": TestData.test_password_1,
         "name": TestData.test_name_2

        }

        requests.post(url, data)
        response = requests.post(url, data)

        user_data = list(response.json().values())[1]

        assert 403 == response.status_code
        assert user_data == "User already exists"

    @allure.title("Проверка невозможности создания пользователя, если одно и полей не заполнено")
    def test_unable_to_create_user_if_one_of_fields_is_not_filled(self, generator):

        email, password, firstName = generator
        url = Endpoints.CREATE_USER
        data = {

         "email": email,
         "password": password,
         "name": TestData.empty_name

        }

        response = requests.post(url, data)
        user_data = list(response.json().values())[1]

        assert 403 == response.status_code
        assert user_data == "Email, password and name are required fields"
