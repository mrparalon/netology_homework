from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
fixed_contact_list = [contacts_list[0]]

for contact in contacts_list[1:]:
    # print(contact[:2])
    lastname, firstname, surname = contact[0], contact[1], contact[2]
    phone = contact[5]
    phone_pattern = r'(\+7|8)\s*\(?(\d+)\)?\s*(\d+)(\s|-)?(\d+)(\s|-)?(\d+)'
    add_phone_pattern = r'Д|доб.?\s?(\d+)'
    name_pattern = r'(\w+)\s+(\w+)(\s+)?(\w+)?'
    
    if not contact[1] or not contact[2]:
        full_name = ' '.join(contact[:2])
        print(full_name)
        parsed_full_name = re.findall(name_pattern, full_name)
        lastname, firstname, surname = \
            parsed_full_name[0][0], parsed_full_name[0][1], parsed_full_name[0][3]
    if phone:
        ph_numbers = re.sub(phone_pattern, r'\2\3\5\7', phone)
        add_number = re.findall(add_phone_pattern, phone)
        fixed_number = '+7'
        fixed_number += f'({ph_numbers[:3]})'
        fixed_number += f'{ph_numbers[3:6]}-{ph_numbers[6:8]}-{ph_numbers[8:10]}'
        print(add_number)
        if add_number:
            fixed_number += f' доб.{add_number[0]}'
        contact[5] = fixed_number
    fixed_contact_list.append(contact)
    
for i in fixed_contact_list:
    print(i)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(fixed_contact_list)