import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester

class TestGetMovie:
    # Запрашиваем афишу
    def test_get_movie(self, created_movie, session_factory, admin_tokens):

        movie = created_movie
        movie_id = movie["id"]
        movie_name = movie["name"]
        movie_location = movie["location"]

        get_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("GET", get_movie_url, None, 200, True)


        # Проверки
        response_data = response.json()
        assert response_data["id"] == movie_id["id"], "id афиш не совпадает"
        assert "id" in response_data, "ID афиши отсутствует в ответе"
        assert response_data["name"] == movie_name["name"], "Название фильма отсутствует в ответе"
        assert response_data["location"] == movie_location["location"], "Место показа фильма отсутствует в афише"


    def test_negative_get_delete_movie(self, auth_admin_headers, created_movie, session_factory, admin_tokens):

        movie = created_movie
        movie_id = movie["id"]

        get_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session)

        requester.send_request("DELETE", get_movie_url, None, 200, False)
        requester.send_request("GET", get_movie_url, None, 404, True)

