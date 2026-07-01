from custom_requester.custom_requester import CustomRequester
from constants import MOVIES_ENDPOINT, BASE_URL



class MoviesApi(CustomRequester):
    """
    Класс для работы с Афишами
    """
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)


    def create_movie(self, movie, expected_status=201):
        return self.send_request(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            data=movie,
            expected_status=expected_status
        )


    def delete_movie(self, movie, expected_status=200):
        movie = movie
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}"

        return self.send_request(
            method="DELETE",
            endpoint=endpoint,
            expected_status=expected_status
        )

    def edit_movie(self, movie, new_data_for_movie, expected_status=200):
        movie = movie
        movie_id = movie["id"]
        body_for_request = {"name": new_data_for_movie["name"], "description": new_data_for_movie["description"]}
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}"

        return self.send_request(
            method="PATCH",
            endpoint=endpoint,
            data=body_for_request,
            expected_status=expected_status
        )


    def get_movie(self, movie, expected_status=200):
        movie = movie
        movie_id = movie["id"]
        endpoint = f"{MOVIES_ENDPOINT}/{movie_id}"

        return self.send_request(
            method="GET",
            endpoint=endpoint,
            expected_status=expected_status
        )

    def get_all_movies(self, params, expected_status=200):
        endpoint = f"{MOVIES_ENDPOINT}/{params}"
        return self.send_request(
            method="GET",
            endpoint=endpoint,
            expected_status=expected_status
        )


