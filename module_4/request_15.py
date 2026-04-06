import requests

from bs4 import BeautifulSoup # Для HTML
import lxml.etree as ET # Для XML

url_html = "https://httpbin.org/html"
response_html = requests.get(url_html)
soup = BeautifulSoup(response_html.text, 'html.parser')
print(soup.title)

url_xml = "https://www.w3schools.com/xml/note.xml"
response_xml = requests.get(url_xml)
tree = ET.fromstring(response_xml.content)
print(tree.find('to').text)