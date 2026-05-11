import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT, REVIEW_ENDPOINT

class TestDeleteReview:
    # Удаляем отзыв
    def test_delete_review(self, auth_admin_headers, created_review):

        response_body = created_review

        movie_id = response_body["id"]

        url_delete_review = f"{BASE_URL}{MOVIES_ENDPOINT}/:{movie_id}{REVIEW_ENDPOINT}"

        response = requests.post(url_create_review, json = created_body_from_review, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка создания отзыва"