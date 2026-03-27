import requests

data = {
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

url = 'https://restful-booker.herokuapp.com/booking'
response = (requests.post(url, json=data))
print(response.json())
assert response.status_code == 200
assert "bookingid" in response.json(), "Ошибка проверки"

