from custom_requester.custom_requester import CustomRequester
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT, BASE_API_URL


class UserApi(CustomRequester):
    """
    Класс для работы с АПИ пользователей.
    """

    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_API_URL)
        self.session = session

