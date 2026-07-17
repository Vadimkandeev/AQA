from constants import BASE_URL, HEADERS, REGISTER_ENDPOINT, LOGIN_ENDPOINT, ADMIN_DATA, USER_ENDPOINT, LOGOUT_ENDPOINT,\
    MOVIES_ENDPOINT, REVIEW_ENDPOINT, BASE_API_URL, GENRES_ENDPOINT
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestGenres:

    def test_created_genres(self, ):