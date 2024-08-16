
import faker

import allure
import random
import string

class FakeData:

    @allure.description('Метод генерации данных с использованием модуля Faker')
    @staticmethod
    def get_sign_up_data():  # выделить в класс


        fake = faker.Faker()

      #  login = fake.text(max_nb_chars=10)

        email = fake.email()
        password = fake.password(6, False, True, False, True)
        firstName = fake.text(max_nb_chars=10)

        return email, password, firstName




        #def generate_random_string(length):
        #    letters = string.ascii_lowercase
        #    random_string = ''.join(random.choice(letters) for i in range(length))
        #    return random_string

        #email = generate_random_string(10)
        #password = generate_random_string(10)
        #firstName = generate_random_string(10)

        #return email, password, firstName

@allure.title('URL и ручки')
class Endpoints:

    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register' # POST Создание юзера

    LOGIN_USER = 'https://stellarburgers.nomoreparties.site/api/auth/login' # POST Авторизация

    LOGOUT_USER = 'https://stellarburgers.nomoreparties.site/api/auth/logout' # POST Выход из системы

    GET_USER_DATA = 'https://stellarburgers.nomoreparties.site/api/auth/user' # GET Получить данные польз.

    EDIT_USER_DATA = 'https://stellarburgers.nomoreparties.site/api/auth/user' # PATCH Изменение данных польз.

    CREATE_ORDER = 'https://stellarburgers.nomoreparties.site/api/orders' # POST Создание заказа

    GET_INGREDIENTS = 'https://stellarburgers.nomoreparties.site/api/ingredients' # GET получить данные об ингредиентах

    GET_ALL_ORDERS = 'https://stellarburgers.nomoreparties.site/api/orders/all' # GET Получить все заказы

    GET_ORDERS_OF_CURRENT_USER = 'https://stellarburgers.nomoreparties.site/api/orders' # GET Получить заказ пользоват.

    UPDATE_TOKEN = 'https://stellarburgers.nomoreparties.site/api/auth/token' # POST Обновление токена refreshToken

    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user' # DELETE Удаление польз.


# requests.exceptions.InvalidSchema: No connection adapters were found for '4https://stellarburgers.nomoreparties.site/api/auth/login'
# - исключение при неверном URL

