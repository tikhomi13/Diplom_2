from data import Endpoints
import requests
import allure
from data import TestData
from data import ResponsesTexts


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_authorized_success(self, create_user_and_login):

        access_token = create_user_and_login
        url_get_ingredients = Endpoints.GET_INGREDIENTS

        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()

        ingredient = r['data'][0]['_id']

        payload = {
            "ingredients": [ingredient]
            }

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.post(url_create_order, payload, headers={'Authorization': access_token})
        data_response = list(response_create_order.json().values())[0]

        assert response_create_order.status_code == 200
        assert ResponsesTexts.success in response_create_order.text
        assert data_response == True

    @allure.title('Создание заказа без авторизации')
    @allure.description('Получаем ингредиент из запроса и сохраняем его в переменную ingredient')
    def test_create_order_unauthorized_(self):

        url_get_ingredients = Endpoints.GET_INGREDIENTS
        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()

        ingredient = r['data'][0]['_id']

        payload = {
            "ingredients": [ingredient]
            }

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.post(url_create_order, payload)
        data_response = list(response_create_order.json().values())[0]

        assert response_create_order.status_code == 200
        assert data_response == True
        assert response_create_order.reason == ResponsesTexts.ok

    @allure.title('Создание заказа c ингредиентом')
    @allure.description('Добываем ингредиент, создаем заказ, добавляем ингредиент')
    def test_create_order_with_ingredients_success(self, create_user_and_login):

        access_token = create_user_and_login

        url_get_ingredients = Endpoints.GET_INGREDIENTS
        response_get_ingredients = requests.get(url_get_ingredients)
        r = response_get_ingredients.json()
        ingredient = r['data'][0]['_id']

        payload = {
            "ingredients": [ingredient]
            }

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.post(url_create_order, payload, headers={'Authorization': access_token})
        data_response = list(response_create_order.json().values())[0]

        assert response_create_order.status_code == 200
        assert data_response == True

    @allure.title('Создание пустого заказа')
    def test_create_empty_order_error(self):

        url_create_order = Endpoints.CREATE_ORDER
        payload = {
            "ingredients": []
        }

        response_create_order = requests.post(url_create_order, json=payload)
        data_response = list(response_create_order.json().values())

        assert response_create_order.status_code == 400
        assert data_response[1] == ResponsesTexts.provide_ingredient

    @allure.title('Создание заказа с неверным хешем')
    def test_create_order_with_wrong_hash_error(self):

        payload_wrong_hash = {

            "ingredients": TestData.wrong_ingredient

        }

        url_create_order = Endpoints.CREATE_ORDER
        response_create_order = requests.post(url_create_order, json=payload_wrong_hash)

        assert response_create_order.status_code == 500
