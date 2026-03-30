import  requests
import pytest


@pytest.fixture
def booking_data():
    return {
    "firstname": "Jim",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2025-01-04",
        "checkout": "2025-01-15"
    },
    "additionalneeds": "Breakfast"
}

@pytest.fixture
def response(booking_data):
    url = 'https://restful-booker.herokuapp.com/booking'

    return requests.post(url, json=booking_data)

def test_create_booking(response, booking_data):
    body = response.json()
    booking = body["booking"]

    assert response.status_code == 200
    assert booking["firstname"] == booking_data["firstname"]



