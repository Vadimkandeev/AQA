from xml.etree import ElementTree as ET
from xml.dom import minidom

INPUT_FILE = "currencies.txt"
OUTPUT_FILE = "KzCurrency.xml"

root = ET.Element("KzCurrency")
root.set("xmlns:int", "http://bssys.com/sbns/integration")

currencies = ET.SubElement(root, "currencies")

with open(INPUT_FILE, encoding="utf-8") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        # Разбиваем по любому количеству пробелов или табуляций
        parts = line.split(maxsplit=2)

        if len(parts) != 3:
            print(f"Пропущена строка: {line}")
            continue

        code, iso_code, name = parts

        curr = ET.SubElement(currencies, "CurrKz")

        ET.SubElement(curr, "code").text = code
        ET.SubElement(curr, "currWithoutCents").text = "false"
        ET.SubElement(curr, "currencyType").text = "3"
        ET.SubElement(curr, "displayOrder").text = "3"
        ET.SubElement(curr, "extId").text = code
        ET.SubElement(curr, "fractDigits").text = "3"
        ET.SubElement(curr, "isoCode").text = iso_code
        ET.SubElement(curr, "name").text = name

xml_string = ET.tostring(root, encoding="utf-8")

pretty_xml = minidom.parseString(xml_string).toprettyxml(
    indent="    ",
    encoding="utf-8"
)

with open(OUTPUT_FILE, "wb") as f:
    f.write(pretty_xml)

print(f"Файл '{OUTPUT_FILE}' успешно создан.")