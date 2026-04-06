import requests

s = requests.Session()

r = s.get('https://httpbin.org/cookies', cookies={"from-my": "browser"})
print(r.text)
print("-" * 20)


r = s.get('https://httpbin.org/cookies')
print(r.text)
print("-" * 20)