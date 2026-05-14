import pytest
import requests
from constants import BASE_URL, MOVIES_ENDPOINT, REVIEW_ENDPOINT



class TestHideReview:
    # Скрываем отзыв на фильм
    def test_hide_review(self, auth_admin_headers, created_review, created_user_by_admin):

        movie_id = created_review

        user_id = created_user_by_admin["id"]

        url_hide_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}/hide/{user_id}"

        response = requests.patch(url_hide_review, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 200, "Ошибка сокрытия отзыва"



# Скрываем отзыв. Ожидается 404
    def test_negative_hide_review(self, auth_admin_headers, created_review, created_user_by_admin):


        movie_id = created_review

        user_id = created_user_by_admin["id"]

        url_hide_review = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}/hide/{user_id}"

        delete_movie_url = f"{BASE_URL}{MOVIES_ENDPOINT}/{movie_id}"

        requests.delete(delete_movie_url, headers=auth_admin_headers)

        response = requests.post(url_hide_review, headers=auth_admin_headers)

        # Логируем ответ для диагностики
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")

        # Проверки
        assert response.status_code == 404, "Ошибка сокрытия отзыва. Ожидается 404"
