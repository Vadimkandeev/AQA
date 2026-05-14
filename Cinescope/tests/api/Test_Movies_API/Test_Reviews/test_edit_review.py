import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT, REVIEW_ENDPOINT
from utils.data_generator import DataGenerator

class TestEditReview:
    # Меняем отзыв на фильм
    def test_edit_review(self, auth_admin_headers, created_review):

        response_body = created_review

        movie_id = response_body["id"]

        new_body = DataGenerator.created_body_for_review()

        url_edit_review = f"{BASE_URL}{MOVIES_ENDPOINT}/:{movie_id}{REVIEW_ENDPOINT}"

        response = requests.put(url_edit_review,json=new_body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка создания отзыва"


    # Меняем отзыв на несуществующий фильм. Ожидается 404
    def test_negative_edit_review(self, auth_admin_headers, created_review):

        response_body = created_review

        movie_id = response_body["id"]

        new_body = DataGenerator.created_body_for_review()

        url_edit_review = f"{BASE_URL}{MOVIES_ENDPOINT}/:{movie_id}{REVIEW_ENDPOINT}"

        requests.delete(url_edit_review, headers=auth_admin_headers)

        response = requests.put(url_edit_review,json=new_body, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 404, "Ошибка редактирования фильма. Ожидается 404"


