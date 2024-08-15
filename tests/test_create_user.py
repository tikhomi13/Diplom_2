import requests
import allure
import pytest

from conftest import generator
#from conftest import create_user

from data import Endpoints
from data import FakeData


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

        response = requests.post(url, data)    # дату не забываем

        print(response.status_code)
        print(response.text)
        print(response.url) # куда послали (итоговый URL адрес)
        print(response.json()) # десериализация
        print(data)


        assert 200 == response.status_code

    @allure.title("Проверка невозможности создания 2-х пользователей с одним email")
    def test_unable_to_create_user_which_is_already_registered_response_403(self):

        url = Endpoints.CREATE_USER

        data = {

         "email": "email_that_already_exists@yandex.ru",
         "password": "123456",
         "name": "Yandex"

        }

        requests.post(url, data)
        response = requests.post(url, data)    # дату не забываем

        print(response.reason)
        print(response.json())

        assert 403 == response.status_code

    @allure.title("Проверка невозможности создания пользователя, если одно и полей не заполнено")
    def test_unable_to_create_user_if_one_of_fields_is_not_filled(self, generator):

        email, password, firstName = generator
        url = Endpoints.CREATE_USER
        data = {

         "email": email,
         "password": password,
         "name": ""

        }

        response = requests.post(url, data)

        print(response.reason)
        print(response.json())

        assert 403 == response.status_code





# Повторение

# import requests

#    response = requests.get('https://qa-mesto.praktikum-services.ru/api/users/me',
#                            headers={'Authorization': 'введи_сюда_свой_токен'})



