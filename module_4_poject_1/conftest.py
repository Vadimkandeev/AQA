import pytest
import requests
from constans import BASE_URL, HEADERS, AUTH_DATA


@pytest.fixture
def auth_session():
    #Create session
    session = requests.Session()
    session.headers.update(HEADERS)

    #Получаем токен
    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json=AUTH_DATA)

    assert response.status_code == 200, "Authorization Error"
    token = response.json().get("token")
    assert token is not None, "Token is not access"


    # Добавляем токен в Cookie
    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture #Невалидный тест с ошибкой авторизации
def invalid_auth_session():
    #Create session
    session = requests.Session()
    session.headers.update(HEADERS)

    #Получаем токен
    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json=INVALID_AUTH_DATA)

    assert response.status_code == 200, "Authorization Error"
    token = response.json().get("token")
    assert token is not None, "Token is not access"


    # Добавляем токен в Cookie
    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture
def booking_data():
    return {
        "firstname": "Ryan",
        "lastname": "Gosling",
        "totalprice": 150000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Piano"
    }


@pytest.fixture
def put_booking_data():
    return {
        "firstname": "Sandra",
        "lastname": "Bullock",
        "totalprice": 2500000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": "Piano"
    }

@pytest.fixture
def patch_booking_data():
    return {
        "firstname": "Ryan",
        "lastname": "Reynolds"
    }


@pytest.fixture
def invalid_type_booking_data():
    return {
        "totalprice": "150000"
    }

@pytest.fixture
def empty_booking_data():
    return {}

@pytest.fixture
def no_required_field_booking_data():
    return {
        "firstname": "Ryan",
        "lastname": "Gosling",
        "totalprice": 150000,
        "depositpaid": True,
        "additionalneeds": "Piano"
    }

@pytest.fixture
def non_exist_field_booking_data():
    return {
        "may_flavor": "rose"
    }
