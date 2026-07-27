from custom_requester.custom_requester import CustomRequester
from constants import REGISTER_ENDPOINT, LOGIN_ENDPOINT, BASE_API_URL, USER_ENDPOINT, BODY_FROM_CHANGE_USER_DATA,\
PARAMS_FOR_GETLIST_MOVIES


class UserApi(CustomRequester):
    """
    Класс для работы с АПИ пользователей.
    """

    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_API_URL, )
        self.session = session


    def get_user_info_for_admin(self, user_id, expected_status=200):
        """
        ПОлучение информации о пользователе.
        :param user_id: АйДи пользователя
        :param expected_status: Ожидаемый статус-код
        """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status = expected_status)


    def delete_user(self, user_id, expected_status=204):
        """
        Удаление пользователя
        :param user_id: АЙДИ пользователя
        :param expected_status: Ожидаемый статус
        :return:
        """


        return self.send_request(
            method="DELETE",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status
        )

    def edit_user_data(self, user_id, expected_status=200):
        """
        Изменение данных пользователя
        :param user_id: АЙДИ пользователя
        :param expected_status: ожидаемый статус
        """
        return self.send_request(
            method="PATCH",
            endpoint=f"{USER_ENDPOINT}/{user_id}",
            data=BODY_FROM_CHANGE_USER_DATA,
            expected_status=expected_status
        )


    def create_user(self, random_user_by_admin, expected_status=201):
        """
        Создание нового пользователя
        :param random_user_by_admin: Данные пользователя
        :param expected_status: Ожидаемый статус
        """
        return self.send_request(
            method="POST",
            endpoint=USER_ENDPOINT,
            data=random_user_by_admin,
            expected_status=expected_status)


    def get_list_users(self, expected_status=200):
        """
        Запрос списка пользователей
        :param expected_status: Ожидаемый статус
        """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}{PARAMS_FOR_GETLIST_MOVIES}",
            expected_status=expected_status
        )






