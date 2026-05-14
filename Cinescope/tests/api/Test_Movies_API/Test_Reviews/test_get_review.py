import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT, REVIEW_ENDPOINT


class TestGetReview:
    # Получаем отзыв на фильм
    def test_get_review(self, auth_admin_headers, created_review):


        movie_id = created_review

        url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"

        response = requests.post(url_create_review, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка создания отзыва"


 # Получаем отзыв на удаленный фильм. Ожидается 404
    def test_negative_get_review(self, auth_admin_headers, created_review):


        movie_id = created_review

        url_create_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        requests.delete(delete_movie_url, headers=auth_admin_headers)

        response = requests.post(url_create_review, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 404, "Ошибка изменения отзыва. Ожидается 404"