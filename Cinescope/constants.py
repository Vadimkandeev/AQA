BASE_URL = "https://auth.dev-cinescope.coconutqa.ru"
BASE_API_URL = "https://api.dev-cinescope.coconutqa.ru"
BASE_PAYMENT_URL = "https://payment.dev-cinescope.coconutqa.ru"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

ADMIN_DATA = {
    "email": "api1@gmail.com",
    "password": "asdqwe123Q"
}

BODY_FROM_CHANGE_USER_DATA = {
    "roles": [
        "USER"
      ],
    "verified": False,
    "banned": True
}

INVALID_REFRESH_TOKEN = "11111111-1111-1111-1111-111111111111"

PARAMS_FOR_GETLIST = "?pageSize=2&page=2&roles=USER&roles=ADMIN&roles=SUPER_ADMIN&createdAt=asc"

LOGIN_ENDPOINT = "/login"
REGISTER_ENDPOINT = "/register"
CONFIRM_ENDPOINT = "/confirm"
LOGOUT_ENDPOINT = "/logout"
REFRESH_TOKENS_ENDPOINT = "/refresh-tokens"
USER_ENDPOINT = "/user"
MOVIES_ENDPOINT = "/movies"
REVIEW_ENDPOINT = "/reviews"
GENRES_ENDPOINT = "/genres"
CREATE_ENDPOINT = "/create"
FIND_ALL_ENDPOINT = "/find-all"

JUNK_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.invalid.signature"