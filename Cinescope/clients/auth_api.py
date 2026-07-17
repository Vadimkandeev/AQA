from custom_requester.custom_requester import CustomRequester
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT, LOGOUT_ENDPOINT,REFRESH_TOKENS_ENDPOINT, CONFIRM_ENDPOINT,\
    BASE_URL, USER_ENDPOINT

class AuthApi(CustomRequester):
    """
    Класс для работы с аутентификацией
    """
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)


    def register_user(self, user_data, expected_status=201):
        """
        Регистрация нового пользователя
        :param user_data: данные пользователя
        :param expected_status: ожидаемый статус-код
        """
        return self.send_request(
            method="POST",
            endpoint=REGISTER_ENDPOINT,
            data=user_data,
            expected_status=expected_status
        )

    def login_user(self, login_data, expected_status=201):
        """
        Авторизация пользователя.
        :param login_data: Данные для логина
        :param expected_status: ожидаемый статус-код
        :return:
        """
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=expected_status
        )

    def authenticate(self, user_creds):
        login_data = {
            "email": user_creds["email"],
            "password": user_creds["password"]
        }

        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]
        self._update_session_headers(**{"authorization": "Bearer " + token})


    def logout_user(self, expected_status=200):
        """
        Разлогин пользователя
        :param expected_status: Ожидаемый статус
        """
        return self.send_request(
         method="GET",
         endpoint=LOGOUT_ENDPOINT,
         expected_status=expected_status
        )


    def refresh_token(self, expected_status=200):
        """
        Обновление refreshToken и accessToken пользователя
        :param expected_status: Ожидаемый статус
        """
        return self.send_request(
            method="GET",
            endpoint=REFRESH_TOKENS_ENDPOINT,
            expected_status=expected_status
        )



    def confirm_email(self, token, expected_status=200):
        """
        Подтверждение имейл
        """
        return self.send_request(
            method="GET",
            endpoint=f"{CONFIRM_ENDPOINT}?token={token}",
            expected_status=expected_status
        )


    def get_user_info_for_user(self, expected_status=200):
        """
               ПОлучение информации о пользователе от имени самого пользователя.
               :param expected_status: Ожидаемый статус-код
               """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}/me",
            expected_status=expected_status)


