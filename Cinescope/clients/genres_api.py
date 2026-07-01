from custom_requester.custom_requester import CustomRequester
from constants import GENRES_ENDPOINT, BASE_URL

class GenresApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def create_genres(self, genre, expected_status=201):
        return self.send_request(
            method="POST",
            data=genre,
            endpoint=GENRES_ENDPOINT,
            expected_status=expected_status
        )



