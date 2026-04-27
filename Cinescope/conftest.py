import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA
import pytest
from utils.data_generator import DataGenerator



@pytest.fixture(scope="function")
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

@pytest.fixture(scope = "function")
def create_user_by_admin(test_user):
    """
    Делаем копию словаря и модифицируем его для запросов раздела "Пользователь"
    """
    new_body = test_user.copy()
    del new_body["passwordRepeat"]
    del new_body["roles"]
    new_body["verified"] = True
    new_body["banned"] = False
    return new_body

# Регистрируем нового пользователя
@pytest.fixture(scope = "function")
def created_user(test_user):
    register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
    response = requests.post(register_url, json=test_user, headers=HEADERS)
    body = response.json()
    print(body)
    assert response.status_code == 201, "Ошибка регистрации пользователя"
    assert body['fullName'] == test_user['fullName']
    return body


# Логинимся для получения токена ПОЛЬЗОВАТЕЛЯ (аутентификация)
@pytest.fixture(scope="function")
def user_tokens(test_user, created_user):
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



# Логинимся для получения токена АДМИНА
@pytest.fixture(scope="function")
def admin_tokens():
    login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
    login_data = ADMIN_DATA
    response = requests.post(login_url, json=login_data, headers=HEADERS)
    assert response.status_code == 200, "Ошибка авторизации"

    # Получаем токен
    data = response.json()
    assert data.get("accessToken"), "accessToken отсутствует в ответе"
    assert data.get("refreshToken"), "refreshToken отсутствует в ответе"
    token = {"accessToken": data.get("accessToken"), "refreshToken": data.get("refreshToken")}
    return token



# Подготавливаем заголовок для АДМИНА с токеном
@pytest.fixture(scope="function")
def auth_admin_headers(admin_tokens):
    return {
        **HEADERS,
        "Authorization": f"Bearer {admin_tokens['accessToken']}"
    }


# Подготавливаем заголовок для ЮЗЕРА с токеном
@pytest.fixture(scope="function")
def auth_user_headers(user_tokens):
    return {
        **HEADERS,
        "Authorization": f"Bearer {user_tokens['accessToken']}"
    }

def build_refresh_cookies(tokens):
    return {
        "refreshToken": tokens["refreshToken"]
    }

# Получаем куки для АДМИНА
@pytest.fixture
def admin_refresh_cookies(admin_tokens):
    return build_refresh_cookies(admin_tokens)

# Получаем куки для ПОЛЬЗОВАТЕЛЯ
@pytest.fixture
def user_refresh_cookies(user_tokens):
    return build_refresh_cookies(user_tokens)


# Cоздаём сессию
@pytest.fixture(scope="session")
def auth_session(tokens):
    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({"Authorization": f"Bearer {tokens['accessToken']}"})
    return session



