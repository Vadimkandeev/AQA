BASE_URL = "https://auth.dev-cinescope.coconutqa.ru"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

ADMIN_DATA = {
    "email": "api1@gmail.com",
    "password": "asdqwe123Q"
}

LOGIN_ENDPOINT = "/login"
REGISTER_ENDPOINT = "/register"
CONFIRM_ENDPOINT = "/confirm"
LOGOUT_ENDPOINT = "/logout"
REFRESH_TOKENS_ENDPOINT = "/refresh-tokens"
USER_ENDPOINT = "/user"

JUNK_TOKEN = "accessToken: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjczNDk2NGVjLTRkNmEtNDc4OS04Mzlm\
LTc1Nzk3MTQxZTczZSIsImVtYWlsIjoiYXBpMUBnbWFpbC5jb20iLCJyb2xlcyI6WyJVU0VSIiwiQURNSU4iLCJTVVBFUl9BRE1JTiJdL\
CJ2ZXJpZmllZCI6dHJ1ZSwiaWF0IjoxNzc3OTA3NDYyLCJleHAiOjE3Nzc5MDkyNjJ9.ntPvcvNVxIpL5XqtehWe4UOugAVJMFL-M-o87R\
5LWZE, refreshToken: c006e50d-e0ab-4a4e-b72f-8a68eea20d44, expiresIn: 1777909262153"