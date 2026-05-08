import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT


class TestDeleteMovie:
    # Запрашиваем афишу
    def test_delete_movie(self, auth_admin_headers, created_movie):

        movie = created_movie
        movie_id = movie["id"]
        movie_name = movie["name"]
        movie_location = movie["location"]

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        response = requests.delete(delete_movie_url, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 200
        assert response.status_code == 200, "Ошибка запроса афиши"
        response_data = response.json()
        assert response_data["id"] == movie_id["id"], "id афиш не совпадает"
        assert "id" in response_data, "ID афиши отсутствует в ответе"
        assert response_data["name"] == movie_name["name"], "Название фильма отсутствует в ответе"
        assert response_data["location"] == movie_location["location"], "Место показа фильма отсутствует в афише"



    def test_negative_delete_movie(self, auth_admin_headers, created_movie):

        movie = created_movie
        movie_id = movie["id"]

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        requests.delete(delete_movie_url, headers=auth_admin_headers)
        response = requests.delete(delete_movie_url, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 404
        assert response.status_code == 404, "Ошибка удаления афиши. Ожидается 404"


