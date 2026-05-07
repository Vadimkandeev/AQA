import pytest
import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, CONFIRM_ENDPOINT, LOGIN_ENDPOINT, LOGOUT_ENDPOINT,REFRESH_TOKENS_ENDPOINT

# Регистрация нового пользователя позитивная проверка
class TestRegistration:
    def test_register_user(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=random_user_by_user, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка регистрации пользователя"
        response_data = response.json()
        assert response_data["email"] == random_user_by_user["email"], "Email не совпадает"
        assert "id" in response_data, "ID пользователя отсутствует в ответе"
        assert "roles" in response_data, "Роли пользователя отсутствуют в ответе"

        # Проверяем, что роль USER назначена по умолчанию
        assert "USER" in response_data["roles"], "Роль USER должна быть у пользователя"


    # Регистрация нового пользователя без поля подтверждения пароля
    def test_negative_register_without_confirm_pass(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле подтверждение пароля)
        body = random_user_by_user.copy()
        del body["passwordRepeat"]

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при отсутствии подтверждения пароля"

    # Регистрация нового пользователя без поля ФИО
    def test_negative_register_without_fullname(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле ФИО)
        body = random_user_by_user.copy()
        del body["fullName"]

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при отсутствии поля ФИО"


    # Регистрация нового пользователя без поля email
    def test_negative_register_without_email(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (удаляем поле email)
        body = random_user_by_user.copy()
        del body["email"]

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при отсутствии поля email"


    # Регистрация нового пользователя с несовпадающими паролями
    def test_negative_register_password_mismatch(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (изменяем повторный пароль)
        body = random_user_by_user.copy()
        body["passwordRepeat"] = "OtherPass12345678"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при несовпадении 'passwordRepeat'"


        # Регистрация нового пользователя с невалидным email
    def test_negative_register_invalid_email(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (делаем невалидный email)
        body = random_user_by_user.copy()
        body["email"] = body["email"].replace("@", "F")

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при невалидном поле 'email'"


        # Регистрация нового пользователя со слишком коротким паролем
    def test_negative_register_short_email(self, random_user_by_user):
        # URL для регистрации
        register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"

        # Фабрикуем невалидное тело запроса (создаем короткий пароль)
        body = random_user_by_user.copy()
        body["password"] = "Q1"
        body["passwordRepeat"] = "Q1"

        # Отправка запроса на регистрацию
        response = requests.post(register_url, json=body, headers=HEADERS)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 400, "Ошибка валидации при слишком коротком пароле"
