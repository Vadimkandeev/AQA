import pytest_test
import requests
from constants import BASE_URL, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester



class TestEditMovie:
    # Создаем афишу
    def test_edit_movie(self, created_movie, created_random_movie, session_factory, admin_tokens):

        edit_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body_for_request = created_movie
        random_body = created_random_movie
        body_for_request["name"] = random_body["name"]
        body_for_request["description"] = random_body["description"]

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        response = requester.send_request("PATCH", edit_movie_url, body_for_request, 200, True)

        # Проверки
        response_data = response.json()

        assert response_data["name"] == random_body["name"], "Названия фильмов не совпадают"
        assert response_data["description"] == random_body["description"], "Описания фильмов не совпадают"
        assert response_data["location"] == random_body["location"], "Места локации фильмов не совпадают"
        assert "id" in response_data, "ID  афиши отсутствует в ответе"


    # Проводим невалидный запрос на создание афиши с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_negative_edit_movie_by_unlegal_token(self, created_random_movie, created_movie, session_factory, user_tokens):
        edit_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}"

        body_for_request = created_movie
        random_body = created_random_movie
        body_for_request["name"] = random_body["name"]
        body_for_request["description"] = random_body["description"]

        admin_session = session_factory(user_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        requester.send_request("PATCH", edit_movie_url, body_for_request, 403, True)

