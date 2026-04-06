import requests


url = "https://httpbin.org/post"

#data = {"key1": "value1", "key2": "value2"}
#data = [("key1", "value1"), ("key2", "value2")]

data = "<xml><data>some data</data></xml>"

response = requests.post(url, data=data)

print(response.request.body)
print("***********************************")
print(response.text)
print("***********************************")

data_bytes = b"raw bytes data"
response_bytes = requests.post(url, data=data_bytes)
print(response.request.body)
print("------------------------------")
print(response.text)
print("------------------------------")
