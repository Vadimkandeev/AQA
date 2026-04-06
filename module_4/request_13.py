import requests


url = "https://httpbin.org/json"
response = requests.get(url)
data = response.json()
print(type(data))
print("-----------------")
print(data)
print("-----------------")
print(data['slideshow']['author'])
print("-----------------")
