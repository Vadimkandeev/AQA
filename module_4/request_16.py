import requests

s = requests.Session()
s.headers.update({'User-Agent': 'My Custom Bot'}) # Постоянный заголовок
s.auth = ('user', 'password') # Постоянная аутентификация

response = s.get('https://httpbin.org/headers')
print(response.json())

response2 = s.post('https://httpbin.org/post', json={"data": "test"})
print(response2.json())