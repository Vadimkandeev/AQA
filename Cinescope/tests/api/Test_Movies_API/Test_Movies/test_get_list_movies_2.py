import pytest_test
import requests
from constants import BASE_URL, MOVIES_ENDPOINT
from custom_requester.custom_requester import CustomRequester



class TestGetListMovie:
    # Запрашиваем афишу
    def test_get_list_movie(self, created_params_for_get_list, session_factory, admin_tokens):

        params = created_params_for_get_list

        get_movie_list_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{params}"

        admin_session = session_factory(admin_tokens)

        requester = CustomRequester(admin_session, BASE_URL)

        # Проверка получения статус-кода. Ожидается 200
        requester.send_request("GET", get_movie_list_url, None, 201, True)




