import re
import os
import copy
from lxml import etree

NAMESPACE = "http://bssys.com/sbns/integration"
NS = {'ns': NAMESPACE}

# ТОЛЬКО ЭТИ ПОЛЯ будут заменены (остальные, включая docNumber и payerAccount, остаются оригинальными)
FIXED_VALUES = {
    'bankAcceptDate': '2026-06-17T17:50:49.082+05:00',
    'benefAccount': 'KZ006014341018367316',
    'benefBankBic': 'HSBKKZKX',
    'benefInn': '430309711000',
    'benefInnFact': '430309711000',
    'benefName': 'АО TestKaz',
    'benefNameFact': 'АО TestKaz',
    'benefOrgType': '17',
    'benefResidentCountry': 'KAZAKHSTAN',
    'chiefAccountant': 'Главный Бухгалтер',
    'currCode': 'KZT',
    #'docDate': '2026-06-17T15:39:00',
    'executive': 'Брежнев Андрей'
}

def process_text_file(input_file, output_dir='output'):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ищем все блоки <IncomingPayment ...> ... </IncomingPayment>
    pattern = r'<IncomingPayment[^>]*>.*?</IncomingPayment>'
    matches = re.findall(pattern, content, re.DOTALL)

    if not matches:
        print("Не найдено ни одного элемента IncomingPayment.")
        return

    for idx, match in enumerate(matches):
        try:
            elem = etree.fromstring(match)
        except etree.XMLSyntaxError as e:
            print(f"Ошибка парсинга фрагмента #{idx+1}: {e}")
            continue

        new_elem = copy.deepcopy(elem)

        # Удаляем только те поля, которые будут заменены
        for tag in FIXED_VALUES.keys():
            for child in new_elem.xpath(f'./ns:{tag}', namespaces=NS):
                new_elem.remove(child)

        # Добавляем новые значения для заменяемых полей
        for tag, value in FIXED_VALUES.items():
            child = etree.SubElement(new_elem, f'{{{NAMESPACE}}}{tag}')
            child.text = value

        # docNumber и payerAccount НЕ трогаем – они остаются оригинальными

        # Сохраняем в отдельный XML-файл
        tree = etree.ElementTree(new_elem)
        filename = os.path.join(output_dir, f'payment_{idx+1:03d}.xml')
        tree.write(filename, encoding='utf-8', xml_declaration=True, pretty_print=True)

    print(f"Обработано {len(matches)} платежей. Файлы сохранены в папку '{output_dir}'.")

if __name__ == '__main__':
    process_text_file('Sourse.txt')