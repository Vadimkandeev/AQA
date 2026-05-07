import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT

class TestCreateUser:
    # Создаем пользователя на стороне админа
    def test_create_user(self, auth_admin_headers, created_random_movie):

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
