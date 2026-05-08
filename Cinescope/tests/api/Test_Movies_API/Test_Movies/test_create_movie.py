import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT

class TestCreateMovie:
    # Создаем афишу
    def test_create_movie(self, auth_admin_headers, created_random_movie):

        create_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body = created_random_movie

        response = requests.post(create_movie_url, json=body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 201, "Ошибка создания афиши"
        response_data = response.json()

        assert response_data["name"] == created_random_movie["name"], "Названия фильмов не совпадают"
        assert response_data["description"] == created_random_movie["description"], "Описания фильмов не совпадают"
        assert response_data["location"] == created_random_movie["location"], "Места локации фильмов не совпадают"
        assert "id" in response_data, "ID  афиши отсутствует в ответе"


    # Проводим невалидный запрос на создание афиши с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_negative_create_movie_by_unlegal_token(self, created_random_movie, auth_user_headers):

        create_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body = created_random_movie

        response = requests.post(create_movie_url, json=body, headers=auth_user_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 403, "Ошибка запроса на создание афиши при невалидном токене.\
           Ожидается статус 403"



    # Проводим невалидный запрос на создание афиши с существующим названием.
    # Вызов статус-кода 409
    def test_negative_create_movie_duplicate_mane(self, created_random_movie, auth_admin_headers):
        create_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body = created_random_movie

        requests.post(create_movie_url, json=body, headers=auth_admin_headers)
        response = requests.post(create_movie_url, json=body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        assert response.status_code == 409, "Ошибка запроса на создание афиши с существующим названием.\
           Ожидается статус 409"
