import pytest_test
import requests
from constants import BASE_API_URL, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester


class TestCreateMovie:
    # Создаем афишу
    def test_create_movie(self, auth_admin_headers, created_random_movie, session_factory, admin_tokens):



        body = created_random_movie

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_API_URL)

        response = requester.send_request("POST", MOVIES_ENDPOINT, body, 201, True)

        #Проверки
        response_data = response.json()

        assert response_data["name"] == created_random_movie["name"], "Названия фильмов не совпадают"
        assert response_data["description"] == created_random_movie["description"], "Описания фильмов не совпадают"
        assert response_data["location"] == created_random_movie["location"], "Места локации фильмов не совпадают"
        assert "id" in response_data, "ID  афиши отсутствует в ответе"


    # Проводим невалидный запрос на создание афиши с токеном пользователя вместо админа.
    # Вызов статус-кода 403
    def test_negative_create_movie_by_unlegal_token(self, auth_admin_headers, created_random_movie, session_factory, user_tokens):



        body = created_random_movie

        admin_session = session_factory(user_tokens)

        requester = CustomRequester(admin_session, BASE_API_URL)

        requester.send_request("POST", MOVIES_ENDPOINT, body, 403, True)



    # Проводим невалидный запрос на создание афиши с существующим названием.
    # Вызов статус-кода 409
    def test_negative_create_movie_duplicate_mane(self, auth_admin_headers, created_random_movie, session_factory, admin_tokens):


        body = created_random_movie

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_API_URL)

        requester.send_request("POST", MOVIES_ENDPOINT, body, 201, False)
        requester.send_request("POST", MOVIES_ENDPOINT, body, 409, True)


