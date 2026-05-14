import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT, REVIEW_ENDPOINT
from utils.data_generator import DataGenerator

class TestCreateReview:
    # Создаем отзыв на фильм
    def test_create_review(self, auth_admin_headers, created_movie):

        response_body = created_movie

        movie_id = response_body["id"]

        body = DataGenerator.created_body_for_review()

        url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"

        response = requests.post(url_create_review, json = body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка создания отзыва"



    # Создаем отзыв на удаленный фильм
    def test_create_review_for_deleted_movie(self, auth_admin_headers, created_movie):
        response_body = created_movie

        movie_id = response_body["id"]

        body = DataGenerator.created_body_for_review()

        url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"
        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        requests.delete(delete_movie_url, headers=auth_admin_headers)
        response = requests.post(url_create_review, json=body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 404, "Ошибка, ожидается 404"


    def test_negative_duplicate_create_review(self, auth_admin_headers, created_movie):

        response_body = created_movie

        movie_id = response_body["id"]

        body = DataGenerator.created_body_for_review()

        url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"

        requests.post(url_create_review, json=body, headers=auth_admin_headers)
        response = requests.post(url_create_review, json=body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 409, "Ошибка проверки на дубликат отзыва. Ожидается 409"