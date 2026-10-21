from constants import  ADMIN_DATA, PARAMS_FOR_GETLIST_MOVIES
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator

from random import randint


class TestPayments:

    def test_create_payment(self, api_manager, auth_admin_headers, created_movie, created_payment_data):

            api_manager.payments_api.headers.update(auth_admin_headers)
            response = api_manager.payments_api.creating_payment(created_payment_data)

            response_data = response.json()


