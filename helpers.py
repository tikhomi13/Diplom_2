import faker
import allure

class FakeData:

    @allure.description('Метод генерации данных с использованием модуля Faker')
    @staticmethod
    def get_sign_up_data():

        fake = faker.Faker()
        email = fake.email()
        password = fake.password(6, False, True, False, True)
        firstName = fake.text(max_nb_chars=10)

        return email, password, firstName


class NewFakeEmail:

    @staticmethod
    def get_new_email():

        fake = faker.Faker()
        new_email = fake.email()
        return new_email