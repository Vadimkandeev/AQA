from custom_requester.custom_requester import CustomRequester
from constants import GENRES_ENDPOINT, BASE_API_URL

class GenresApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_API_URL)

    def created_genres(self, genre_body, expected_status=201):
        return self.send_request(
            method="POST",
            data=genre_body,
            endpoint=GENRES_ENDPOINT,
            expected_status=expected_status
        )

    def deleted_genre(self, new_genre, expected_status=200):
        genre_id = new_genre["id"]
        endpoint = f"{GENRES_ENDPOINT}/{genre_id}"
        return self.send_request(
            method="DELETE",
            endpoint=endpoint,
            expected_status=expected_status
        )


    def get_list_genres(self, expected_status=200):
        return self.send_request(
            method="GET",
            endpoint=GENRES_ENDPOINT,
            expected_status=expected_status
        )


    def get_one_genre(self, new_genre, expected_status=200):
        genre_id = new_genre["id"]
        endpoint = f"{GENRES_ENDPOINT}/{genre_id}"
        return self.send_request(
            method="GET",
            endpoint=endpoint,
            expected_status=expected_status
        )





