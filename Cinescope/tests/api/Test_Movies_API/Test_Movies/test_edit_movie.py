import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT



class TestEditMovie:
    # Создаем афишу
    def test_edit_movie(self, auth_admin_headers, created_movie, created_random_movie):

        edit_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body_for_request = created_movie
        random_body = created_random_movie
        body_for_request["name"] = random_body["name"]
        body_for_request["description"] = random_body["description"]

        response = requests.patch(edit_movie_url, json=body_for_request, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка редактирования афиши"
        response_data = response.json()

        assert response_data["name"] == random_body["name"], "Названия фильмов не совпадают"
        assert response_data["description"] == random_body["description"], "Описания фильмов не совпадают"
        assert response_data["location"] == random_body["location"], "Места локации фильмов не совпадают"
        assert "id" in response_data, "ID  афиши отсутствует в ответе"


    # Проводим невалидный запрос на создание афиши с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_negative_edit_movie_by_unlegal_token(self, created_random_movie, auth_user_headers, created_movie):
        edit_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body_for_request = created_movie
        random_body = created_random_movie
        body_for_request["name"] = random_body["name"]
        body_for_request["description"] = random_body["description"]

        response = requests.patch(edit_movie_url, json=body_for_request, headers=auth_user_headers)

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