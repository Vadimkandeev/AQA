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

response = requests.post(url, json=data)
my_dict = response.json()

print(response.status_code)
print(my_dict["bookingid"])
print(response.json()['booking']['lastname'])

assert  response.status_code == 200, "Errore code"
assert my_dict["bookingid"]
assert response.json()['booking']['lastname']