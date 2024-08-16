import requests
import allure
from data import Endpoints


class TestEditUserData:

    def test_edit_data_user_authorized_success(self, generator):

        # Создаем пользователя

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

        refresh_token = r['refreshToken']
        print(refresh_token)

        # Меняем данные

        url_change_data = Endpoints.EDIT_USER_DATA

        update_data = {

            "email": f'new_{email}',   # Меняем Email
            "password": "123456",      # Меняем пароль
            "name": "new_user_name"    # Меняем имя

        }

        response_edit_data = requests.patch(url_change_data, update_data, headers={'Authorization': access_token})
        print(response_edit_data.status_code)
        print(response_edit_data.reason)
        print(response_edit_data.json())

        assert response_edit_data.status_code == 200

        # спросить как передать токен авторизации из фикстуры в тест чтобы не дублировать код и убрать его в фикстуру

        # добавить в ридми гайд по ошибке fixture 'generator' not found - что зайти в конфиг и убрать тестс

    def test_edit_data_user_unauthorized_unable_to_edit(self, generator):

        # Создаем пользователя

        url = Endpoints.CREATE_USER
        email, password, firstName = generator
        data = {

            "email": email,
            "password": password,
            "name": firstName

        }

        response_register = requests.post(url, data)
        print(response_register.status_code)

        # меняем данные

        url_change_data = Endpoints.EDIT_USER_DATA
        update_data = {

            "email": f'new_{email}',   # Меняем Email
            "password": "123456",      # Меняем пароль
            "name": "new_user_name"    # Меняем имя

        }

        response_edit_data = requests.patch(url_change_data, update_data) # не передаем токен авторизации
        print(response_edit_data.status_code)
        print(response_edit_data.reason)
        print(response_edit_data.json())

        assert 401 == response_edit_data.status_code      # Проверяем, что система вернула ошибку
        assert 'Unauthorized' == response_edit_data.reason











#        print(response_edit_data.reason)
#        print(response_edit_data.text)
#        print(response_edit_data.url) # куда послали (итоговый URL адрес)
#        print(data)
#        print(response_edit_data.json())










