import requests
from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/passwd"  # URL, требующий Basic Auth

response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))

print(f"Status code: {response.status_code}")
print(response.json())