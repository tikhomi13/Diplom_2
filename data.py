class Endpoints:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/'

    CREATE_USER = f'{BASE_URL}api/auth/register' # POST Создание юзера

    LOGIN_USER = f'{BASE_URL}api/auth/login' # POST Авторизация

    LOGOUT_USER = f'{BASE_URL}api/auth/logout' # POST Выход из системы

    GET_USER_DATA = f'{BASE_URL}api/auth/user' # GET Получить данные польз.

    EDIT_USER_DATA = f'{BASE_URL}api/auth/user' # PATCH Изменение данных польз.

    CREATE_ORDER = f'{BASE_URL}api/orders' # POST Создание заказа

    GET_INGREDIENTS = f'{BASE_URL}api/ingredients' # GET получить данные об ингредиентах

    GET_ALL_ORDERS = f'{BASE_URL}api/orders/all' # GET Получить все заказы

    GET_ORDERS_OF_CURRENT_USER = f'{BASE_URL}api/orders' # GET Получить заказ пользоват.

    UPDATE_TOKEN = f'{BASE_URL}api/auth/token' # POST Обновление токена refreshToken

    DELETE_USER = f'{BASE_URL}api/auth/user' # DELETE Удаление польз.


class TestData:

    email_that_already_exists = "email_that_already_exists@yandex.ru"
    unexisting_email = "this_email_does_not_exist@yandex.jj"
    test_password_1 = '123456'
    test_name_1 = 'name'
    test_name_2 = 'Yandex'
    empty_name = ''
    wrong_ingredient = '["wrong_ingredient"]'
    new_user_name = "new_user_name"
    unauthorized_message = 'Unauthorized'
    you_should_be_authorised_message = 'You should be authorised'


class ResponsesTexts:

    user_exists = "User already exists"
    fields_required = "Email, password and name are required fields"
    success = "success"
    ok = "OK"
    provide_ingredient = "Ingredient ids must be provided"
    unauthorized = 'Unauthorized'
    wrong_email_or_password = "email or password are incorrect"
