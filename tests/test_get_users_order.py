import requests
import allure
from data import Endpoints
from data import TestData


class TestGetOrders:

    @allure.title('Получение заказов с авторизацией')
    @allure.description('Передаем токен пользователя, получаем список заказов')
    def test_get_orders_authorized_success(self, create_user_and_login):

        access_token = create_user_and_login
        url_get_users_orders = Endpoints.GET_ORDERS_OF_CURRENT_USER
        response_get_orders = requests.get(url_get_users_orders, headers={'Authorization': access_token})

        data_response = list(response_get_orders.json().values())[0]

        assert response_get_orders.status_code == 200
        assert data_response == True

    @allure.title('Получение заказов без авторизации')
    @allure.description('Получаем 401 You should be authorised')
    def test_get_orders_unauthorized_success(self):

        url_get_users_orders = Endpoints.GET_ORDERS_OF_CURRENT_USER
        response = requests.get(url_get_users_orders)

        assert response.status_code == 401
        assert response.reason == TestData.unauthorized_message
        assert response.json()['message'] == TestData.you_should_be_authorised_message
