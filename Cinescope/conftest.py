import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT
import pytest
from utils.data_generator import DataGenerator


@pytest.fixture(scope="session")
def test_user():
    """
    Генерация случайного пользователя для тестов.
    """
    random_email = DataGenerator.generate_random_email()
    random_name = DataGenerator.generate_random_name()
    random_password = DataGenerator.generate_random_password()

    return {
        "email": random_email,
        "fullName": random_name,
        "password": random_password,
        "passwordRepeat": random_password,
        "roles": ["USER"]
    }


# Регистрируем нового пользователя
@pytest.fixture(scope = "session")
def created_user(test_user):
    register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
    response = requests.post(register_url, json=test_user, headers=HEADERS)
    body = response.json()
    assert response.status_code == 201, "Ошибка регистрации пользователя"
    assert body['fullName'] == test_user['fullName']
    return body


# Логинимся для получения токена (аутентификация)
@pytest.fixture(scope="session")
def tokens(test_user, created_user):
    login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
    login_data = {
        "email": test_user["email"],
        "password": test_user["password"]
    }
    response = requests.post(login_url, json=login_data, headers=HEADERS)
    assert response.status_code == 200, "Ошибка авторизации"

    # Получаем токен
    data = response.json()
    assert data.get("accessToken"), "accessToken отсутствует в ответе"
    assert data.get("refreshToken"), "refreshToken отсутствует в ответе"
    token = {"accessToken": data.get("accessToken"), "refreshToken": data.get("refreshToken")}
    return token


# Cоздаём сессию
@pytest.fixture(scope="session")
def auth_session(tokens):
    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({"Authorization": f"Bearer {tokens['accessToken']}"})
    return session



