from data import Endpoints
import requests
import allure

class TestCreateOrder:

    def test_create_order_authorized_success(self, generator):

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
        access_token = r['accessToken']
        print(access_token)

        refresh_token = r['refreshToken']
        print(refresh_token)

        # Авторизуемся

        data_login = {
            "email": email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response_login = requests.post(url_login, data_login, headers={'Authorization': access_token})

        print(response_login.status_code)

        # Добываем ингредиент

        url_get_ingredients = Endpoints.GET_INGREDIENTS

        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()

        ingredient = r['data'][0]['_id']   # Получаем ингредиент
        print(ingredient)

        # Создаем заказ

        url_create_order = Endpoints.CREATE_ORDER

        response_create_order = requests.get(url_create_order, ingredient, headers={'Authorization': access_token})   # Добавить авторизацию

        print(response_create_order.json())
        print(response_create_order.status_code)

        assert response_create_order.status_code == 200

    def test_create_order_unauthorized_(self):   #?????(self)

        url_get_ingredients = Endpoints.GET_INGREDIENTS

        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()

        ingredient = r['data'][0]['_id']   # Получаем ингредиент
        print(ingredient)

        url_create_order = Endpoints.CREATE_ORDER

        response_create_order = requests.get(url_create_order, ingredient)

        print(response_create_order.json())
        print(response_create_order.status_code)

        assert response_create_order.status_code == 401

    def test_create_order_with_ingredients_success(self, generator):

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
        access_token = r['accessToken']
        print(access_token)

        refresh_token = r['refreshToken']
        print(refresh_token)

        # Авторизуемся

        data_login = {
            "email": email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response_login = requests.post(url_login, data_login, headers={'Authorization': access_token})

        print(response_login.status_code)

        # Добываем ингредиент

        url_get_ingredients = Endpoints.GET_INGREDIENTS

        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()

        ingredient = r['data'][0]['_id']   # Получаем ингредиент
        print(ingredient)

        # Создаем заказ, добавляем ингредиент

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.get(url_create_order, ingredient, headers={'Authorization': access_token})   # Добавить авторизацию

        print(response_create_order.json())
        print(response_create_order.status_code)

        assert response_create_order.status_code == 200

    def test_create_empty_order_error(self):   # тут была ошибка потмоу что перепутал POST И GET !

        # Создаем заказ

        url_create_order = Endpoints.CREATE_ORDER

        payload = {
            "ingredients": []
        }

        response_create_order = requests.post(url_create_order, json=payload)   # Добавить авторизацию

        print(response_create_order.json())
        print(response_create_order.status_code)

        assert response_create_order.status_code == 400

    def test_create_order_with_wrong_hash_error(self):

        payload_wrong_hash = {

            "ingredients": ["wrong_ingredient"]

        }

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.post(url_create_order, json=payload_wrong_hash)   # Добавить авторизацию
        print(response_create_order.status_code)

        assert response_create_order.status_code == 500



