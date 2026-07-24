from constants import  ADMIN_DATA, PARAMS_FOR_GETLIST
import pytest
from random import randint
from api.api_manager import ApiManager
from utils.data_generator import DataGenerator


class TestPayments:

    def test_create_payment(self, api_manager.):