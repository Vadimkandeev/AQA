from custom_requester.custom_requester import CustomRequester
from constants import BASE_PAYMENT_URL, CREATE_ENDPOINT, USER_ENDPOINT, FIND_ALL_ENDPOINT

class PaymentApi(CustomRequester):
    """
    Класс для работы с аутентификацией
    """
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_PAYMENT_URL)


    # Создание платежа
    def creating_payment(self, payment_data, expected_status=201):
        """
        Создание платежа
        :param payment_data: данные кредитной карты
        :param expected_status: Ожидаемый статус
        """

        return self.send_request(
            method="POST",
            endpoint=CREATE_ENDPOINT,
            data=payment_data,
            expected_status=expected_status
        )



    # Получение списка платежей пользователя на правах админа
    def get_user_payments_by_admin(self, user_id, expected_status=200):
        """
        Получение списка платежей пользователя
        :param user_id:  Айди пользователя
        :param expected_status:  Ожидаемый статус
        """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}{USER_ENDPOINT}/{user_id}",
            expected_status=expected_status
        )


    # Получение списка платежей пользователя на правах пользователя
    def get_user_payments_by_(self, expected_status=200):
        """
        Получение списка платежей пользователя
        :param expected_status:  Ожидаемый статус
        """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}{USER_ENDPOINT}",
            expected_status=expected_status
        )


    # Получение списка всех платежей
    def get_all_payments(self, params, expected_status=200):
        """
        Получение списка платежей пользователя
        :param params: параметр запроса
        :param expected_status:  Ожидаемый статус
        """
        return self.send_request(
            method="GET",
            endpoint=f"{USER_ENDPOINT}{USER_ENDPOINT}/{params}",
            expected_status=expected_status #+++++++++++++++++++++++++++++++++++++++++++++++++
        )
