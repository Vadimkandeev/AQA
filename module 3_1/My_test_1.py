import requests

def test_google():
    response = requests.get("https://google.com")
    assert response.status_code == 200


