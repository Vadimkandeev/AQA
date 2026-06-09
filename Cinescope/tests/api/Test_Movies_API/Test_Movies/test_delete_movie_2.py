import pytest_test
import requests
from constants import BASE_URL, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class TestDeleteMovie:
    # Запрашиваем афишу
    def test_delete_movie(self, created_movie, session_factory, admin_tokens):

        movie = created_movie
        movie_id = movie["id"]
        movie_name = movie["name"]
        movie_location = movie["location"]

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("DELETE", delete_movie_url, None, 200, True)

        # Проверка получения статус-кода. Ожидается 200
        assert response.status_code == 200, "Ошибка запроса афиши"
        response_data = response.json()
        assert response_data["id"] == movie_id["id"], "id афиш не совпадает"
        assert "id" in response_data, "ID афиши отсутствует в ответе"
        assert response_data["name"] == movie_name["name"], "Название фильма отсутствует в ответе"
        assert response_data["location"] == movie_location["location"], "Место показа фильма отсутствует в афише"



    def test_negative_delete_movie(self, auth_admin_headers, created_movie, session_factory, admin_tokens):

        movie = created_movie
        movie_id = movie["id"]

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requests.delete(delete_movie_url, headers=auth_admin_headers)
        requester.send_request("DELETE", delete_movie_url, None, 404, True)



