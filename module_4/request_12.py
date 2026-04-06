import requests

url = "https://httpbin.org/encoding/utf8"  # Пример, где httpbin сообщает кодировку utf-8
response = requests.get(url)

print(f"Кодировка до изменения: {response.encoding}")
print(f"Текст до изменения:\n{response.text}")

response.encoding = 'utf-8'  # Явно устанавливаем utf-8 (в данном случае это избыточно, так как httpbin уже указал эту кодировку)
print(f"Кодировка после изменения: {response.encoding}")
print(f"Текст после изменения:\n{response.text}")

url_latin = "https://httpbin.org/encoding/utf8" # Пример, где мы *ошибочно* предполагаем latin1
response_latin = requests.get(url_latin)
response_latin.encoding = 'latin1' # *Неправильная* кодировка, приведет к искажению текста
print(f"Текст с (неправильной) кодировкой latin1:\n{response_latin.text}")

# Правильный подход:
response_latin_correct = requests.get(url_latin)
response_latin_correct.encoding = response_latin_correct.apparent_encoding # используем apparent_encoding
print(f"Текст с (автоматически определенной) кодировкой:\n{response_latin_correct.text}")