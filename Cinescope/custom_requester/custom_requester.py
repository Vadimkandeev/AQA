import json
import requests
import logging
import os

class CustomerRequester:
    """
    Кастомный реквестер для стандартизации и упрощения отправки HTTP запросов
    """

    base_headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
    }

    def __init__(self, sesion, base_url):
        """
        Инициализация кастомного реквестера.
        :param sesion: Объект requests.Session.
        :param base_url: Базовый URL API
        """
        self.session = sesion
        self.base_url = base_url
        self.headers = self.base_headers.copy()
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_request(self, method, endpoint, data = None, params = None, expected_status = 200, need_logging = True):
        """
        Универсальный метод отправки запросов
        :param method:
        :param endpoint:
        :param data:
        :param params:
        :param expected_status:
        :param need_logging:
        :return:
        """
        url = f"{self.base_url}{endpoint}"