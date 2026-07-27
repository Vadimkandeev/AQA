from clients.user_api import UserApi
from clients.auth_api import AuthApi
from clients.genres_api import GenresApi
from clients.review_api import ReviewsApi
from clients.movies_api import  MoviesApi
from payments.payment_api import PaymentApi


class ApiManager:
    """
    Класс для управления API классами с единой HTTP сессией
    """
    def __init__(self, session):
        """
        Инициализация ApiManager
        :param session: HTTP -сессия, используемая всеми API классами
        """
        self.session = session
        self.auth_api = AuthApi(session)
        self.user_api = UserApi(session)
        self.genres_api = GenresApi(session)
        self.review_api = ReviewsApi(session)
        self.movies_api = MoviesApi(session)
        self.payments_api = PaymentApi(session)
