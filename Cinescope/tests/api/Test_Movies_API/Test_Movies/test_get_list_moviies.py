import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT



class TestGetListMovie:
    # Запрашиваем афишу
    def test_get_list_movie(self, created_params_for_get_list, auth_admin_headers):

        params = created_params_for_get_list

        get_movie_list_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{params}"

        response = requests.get(get_movie_list_url, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 200
        assert response.status_code == 200, "Ошибка запроса афиши"



    def test_negative_get_list_movie(self, auth_admin_headers, created_params_for_get_list):

        params = created_params_for_get_list

        get_movie_list_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{params}"

        response = requests.get(get_movie_list_url, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверка получения статус-кода. Ожидается 404
        assert response.status_code == 404, "Ошибка запроса афиши.Ожидается 404"

