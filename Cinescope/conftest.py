import requests
from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT
import pytest
from utils.data_generator import DataGenerator
from random import randint

@pytest.fixture(scope="function")
def random_user_by_user():
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
def random_user_by_admin(random_user_by_user):
    """
    Делаем копию словаря и модифицируем его для запросов раздела "Пользователь"
    """
    new_body = random_user_by_user.copy()
    del new_body["passwordRepeat"]
    del new_body["roles"]
    new_body["verified"] = True
    new_body["banned"] = False
    return new_body

# Создаем нового пользователя от имени пользователя
@pytest.fixture(scope = "function")
def created_user_by_user(random_user_by_user):
    register_url = f"{BASE_URL}{REGISTER_ENDPOINT}"
    response = requests.post(register_url, json=random_user_by_user, headers=HEADERS)
    body = response.json()
    print(body)
    assert response.status_code == 201, "Ошибка регистрации пользователя"
    assert body['fullName'] == random_user_by_user['fullName']
    return body


# Создаем нового пользователя от имени админа
@pytest.fixture(scope = "function")
def created_user_by_admin(random_user_by_admin, auth_admin_headers):
    register_url = f"{BASE_URL}{USER_ENDPOINT}"
    response = requests.post(register_url, json=random_user_by_admin, headers=auth_admin_headers)
    body = response.json()
    print(body)
    assert response.status_code == 201, "Ошибка регистрации пользователя"
    assert body['fullName'] == random_user_by_admin['fullName']
    return body


# Логинимся для получения токена ПОЛЬЗОВАТЕЛЯ (аутентификация)
@pytest.fixture(scope="function")
def user_tokens(random_user_by_user, created_user_by_user):
    login_url = f"{BASE_URL}{LOGIN_ENDPOINT}"
    login_data = {
        "email": random_user_by_user["email"],
        "password": random_user_by_user["password"]
    }
    response = requests.post(login_url, json=login_data, headers=HEADERS)

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
        "Test_Authorization": f"Bearer {admin_tokens['accessToken']}"
    }



# Подготавливаем заголовок для ЮЗЕРА с токеном
@pytest.fixture(scope="function")
def auth_user_headers(user_tokens):
    return {
        **HEADERS,
        "Test_Authorization": f"Bearer {user_tokens['accessToken']}"
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


# Проводим разлогин для негативной проверки Обновления токена
@pytest.fixture(scope="session")
def logout_user(user_tokens):
    logout_url = f"{BASE_URL}{LOGOUT_ENDPOINT}"
    response = requests.get(logout_url, headers=HEADERS)
    assert response.status_code == 200, "Ошибка выхода из учетной записи"



# Создаем тело запроса для создания киноафиши
@pytest.fixture(scope = "session")
def created_random_movie():
    movie_name = DataGenerator.generate_random_movie_name()
    movie_description = DataGenerator.generate_random_movie_description()
    body = {
      "name": movie_name,
      "imageUrl": "https://image.url",
      "price": 100,
      "description": movie_description,
      "location": "SPB",
      "published": True,
      "genreId": 1
    }
    return body


#Создание афиши
@pytest.fixture(scope = "session")
def created_movie(created_random_movie, auth_admin_headers):
    create_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

    body = created_random_movie

    response = requests.post(create_movie_url, json=body, headers=auth_admin_headers)

    # Логируем ответ для диагностики
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")

    # Проверки
    assert response.status_code == 201, "Ошибка создания афиши"
    response_data = response.json()
    return response_data


# Удаление афиши
@pytest.fixture(scope = "session")
def delete_movie(auth_admin_headers, created_movie):
    movie = created_movie
    movie_id = movie["id"]

    delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

    response = requests.delete(delete_movie_url, headers=auth_admin_headers)

    # Логируем ответ для диагностики
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")

    # Проверка получения статус-кода. Ожидается 200
    assert response.status_code == 200, "Ошибка удаления афиши"


# Создаем строку параметров для запроса списка афиш
@pytest.fixture(scope = "session")
def created_params_for_get_list():
    params = f"?pageSize={randint(1, 10)}&page={randint(1, 5)}&minPrice={randint(1, 2)}\
    &maxPrice={randint(20, 1000)}&locations=MSK&locations=SPB&published=true&genreId=1&createdAt=asc"
    return params


# Создаем отзыв о фильме
@pytest.fixture(scope = "session")
def created_review(auth_admin_headers, created_movie, created_body_from_review):

    response_body = created_movie

    movie_id = response_body["id"]

    url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/:{movie_id}{REVIEW_ENDPOINT}"

    response = requests.post(url_create_review, json=created_body_from_review, headers=auth_admin_headers)

    # Проверки
    assert response.status_code == 200, "Ошибка создания отзыва"

# Cоздаём сессию
@pytest.fixture(scope="session")
def auth_session(user_tokens):
    session = requests.Session()
    session.headers.update(HEADERS)
    session.headers.update({"Test_Authorization": f"Bearer {user_tokens['accessToken']}"})
    return session



