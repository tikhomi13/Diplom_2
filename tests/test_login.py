import requests
from data import Endpoints
import allure
from data import TestData


class TestLogin:

    @allure.title('Логин под существующим пользователем')
    def test_login_under_existing_user_success_login(self, create_user, generator):

        email, password, firstName = generator
        access_token = create_user

        data_login = {
            "email": email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response_login = requests.post(url_login, data_login, headers={'Authorization': access_token})

        assert response_login.status_code == 200

    @allure.title('Логин с неверным логином и паролем')
    @allure.description('Передаем несуществующий email, получаем 401')
    def test_login_under_unexisting_user_unable_to_login(self, create_user, generator):

        email, password, firstName = generator
        access_token = create_user

        data_login = {
            "email": TestData.unexisting_email,
            "password": password
        }

        url_login = Endpoints.LOGIN_USER
        response = requests.post(url_login, data_login, headers={'Authorization': access_token})

        assert response.status_code == 401
