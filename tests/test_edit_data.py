import requests
import allure
from data import Endpoints
from data import TestData
from helpers import NewFakeEmail


class TestEditUserData:

    @allure.title('Изменение данных авторизованного пользователя')
    @allure.description('Создаем пользователя, затем меняем email, пароль и имя')
    def test_edit_data_user_authorized_success(self, create_user):

        new_email = NewFakeEmail.get_new_email()

        access_token = create_user
        url_change_data = Endpoints.EDIT_USER_DATA

        update_data = {

            "email": new_email,
            "password": TestData.test_password_1,
            "name": TestData.new_user_name

        }

        response_edit_data = requests.patch(url_change_data, update_data, headers={'Authorization': access_token})

        data_response = list(response_edit_data.json().values())[1]

        assert response_edit_data.status_code == 200
        assert new_email in list(data_response.values())[0]

    @allure.title('Изменение данных Неавторизованного пользователя')
    @allure.description('Не передаем токен авторизации, проверяем, что вернулся код 401')
    def test_edit_data_user_unauthorized_unable_to_edit(self, create_user, generator):

        email = generator
        url_change_data = Endpoints.EDIT_USER_DATA
        update_data = {

            "email": f'new_{email}',
            "password": TestData.test_password_1,
            "name": TestData.new_user_name

        }

        response_edit_data = requests.patch(url_change_data, update_data)
        assert 401 == response_edit_data.status_code
        assert 'Unauthorized' == response_edit_data.reason
