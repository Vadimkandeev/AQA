from custom_requester.custom_requester import CustomRequester
from constants import MOVIES_ENDPOINT, BASE_API_URL, REVIEW_ENDPOINT


class ReviewsApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_API_URL)

    def created_review(self, movie, data_review, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"
        return self.send_request(
            method="POST",
            data=data_review,
            endpoint=endpoint,
            expected_status=expected_status
        )

    def deleted_review(self, movie, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"
        return self.send_request(
            method="DELETE",
            endpoint=endpoint,
            expected_status=expected_status
        )


    def edited_review(self, movie, new_data, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"
        return self.send_request(
            method="PUT",
            data=new_data,
            endpoint=endpoint,
            expected_status=expected_status
        )


    def get_review(self, movie, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}"
        return self.send_request(
            method="GET",
            endpoint=endpoint,
            expected_status=expected_status
        )


    def show_review(self, movie, user_id, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}/show/{user_id}"
        return self.send_request(
            method="PATCH",
            endpoint=endpoint,
            expected_status=expected_status
        )


    def hide_review(self, movie, user_id, expected_status=200):
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}{REVIEW_ENDPOINT}/hide/{user_id}"
        return self.send_request(
            method="PATCH",
            endpoint=endpoint,
            expected_status=expected_status
        )





