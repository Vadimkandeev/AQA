import pytest
import requests
from constants import BASE_URL, HEADERS,  USER_ENDPOINT


class TestDelUser:
    def test_del_user(self, test_create_user):
