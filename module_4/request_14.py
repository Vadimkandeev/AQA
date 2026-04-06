import requests


urls = [
    "https://httpbin.org/json",  # Нормальный JSON
    "https://httpbin.org/status/204", # Пустой ответ
    "https://httpbin.org/status/500",  # Ошибка 500
    "https://httpbin.org/html", # HTML
]

for url in urls:
    print(f"URL: {url}")
    response = requests.get(url)
    data = response.json()
    print(data)
    print("-" * 20)
