import requests


url = "https://httpbin.org/get"

response = requests.get(url)

if response.status_code == 200:
    print(f"Текст ответа: \n{response.text}")
else:
    print(f"Ошибка запроса: \n{response.status_code}")
    print(f"Текст ошибки: \n{response.text}")