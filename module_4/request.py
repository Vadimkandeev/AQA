import requests


# response = requests.get('https://restful-booker.herokuapp.com/booking')
#
# print(f"Статус ответа: {response.status_code}")
# print(f"Тело ответа: {response.text}")
# booking_id = 1
# response = requests.get(f'https://restful-booker.herokuapp.com/booking/', params={'firstname': 'Sally'})
# data = response.json()
#
# #print(f"можно обратиться по ключу, например к первому элементу: {data[0]}")
# print(f"Тело ответа: {data}")

import requests

# делаем словарь для отправки
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

# отправляем наш запрос
response = requests.post(
    'https://restful-booker.herokuapp.com/booking', json=data)

print(response.json())