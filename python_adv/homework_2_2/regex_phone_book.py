from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

class PhoneBook:
    def __init__(self):
        self.csv_headers = ('lastname','firstname','surname','organization','position','phone','email')
        self.phonebook_contacts = []

    def generate_contacts(self, contacts_list):
        for contact in contacts_list:
            self.phonebook_contacts.append(Contact(contact))

    def find_and_merge_similar(self):
        similar_contacts_list = self.find_similar_contacts()
        merged_contact_list = []
        new_phonebook_contacts = []
        for contact_pair in similar_contacts_list:
            merged_contact = self.merge_similar_contacts(contact_pair)
            self.phonebook_contacts.remove(contact_pair[0])
            self.phonebook_contacts.remove(contact_pair[1])
            self.phonebook_contacts.append(merged_contact)




    def find_similar_contacts(self):
        similar_contacts_list = []
        for i, contact in enumerate(self.phonebook_contacts):
            for other_contact in self.phonebook_contacts[i+1:]:
                if contact.is_similar(other_contact):
                    similar_contacts_list.append((contact, other_contact))
        return similar_contacts_list

    def merge_similar_contacts(self, similar_contacts):
        contact_1, contact_2 = similar_contacts[0], similar_contacts[1]
        if not contact_1.surname and contact_2.surname:
            contact_1.surname = contact_2.surname
        if not contact_1.position and contact_2.position:
            contact_1.position = contact_2.position
        if not contact_1.phone and contact_2.phone:
            contact_1.phone = contact_2.phone 
        if not contact_1.email and contact_2.email:
            contact_1.email = contact_2.email
        return contact_1
    
    def get_list(self):
        contacts_list = [list(self.csv_headers)]
        for contact in self.phonebook_contacts:
            contact_for_csv = [[contact.lastname, contact.firstname,
            contact.surname, contact.organization, contact.position,
            contact.phone, contact.email]]
            contacts_list += contact_for_csv
        return contacts_list


    


class Contact:
    def __init__(self, contact_info):
        contact_info = self.normalize_name(contact_info)
        contact_info = self.normalize_phone(contact_info)
        self.lastname = contact_info[0]
        self.firstname = contact_info[1]
        self.surname = contact_info[2]
        self.organization = contact_info[3]
        self.position = contact_info[4]
        self.phone = contact_info[5]
        self.email = contact_info[6]

    def __str__(self):
        return f'{self.lastname} {self.firstname} {self.surname} {self.phone}'

    def is_similar(self, other):
        result = False
        if self.lastname == other.lastname and self.firstname == other.firstname:
            result = True
            if self.surname and other.surname:
                if self.surname != other.surname:
                    result = False 
        return result



    def normalize_name(self, contact_info):
        name_pattern = r'(\w+)\s+(\w+)(\s+)?(\w+)?'
        if not contact_info[1] or not contact_info[2]:
            full_name = ' '.join(contact_info[:2])
            parsed_full_name = re.findall(name_pattern, full_name)
            lastname, firstname, surname = \
                parsed_full_name[0][0], parsed_full_name[0][1], parsed_full_name[0][3]
            contact_info[0], contact_info[1], contact_info[2] = lastname, firstname, surname
        return contact_info

    def normalize_phone(self, contact_info):
        phone_pattern = r'(\+7|8)\s*\(?(\d+)\)?\s*(\d+)(\s|-)?(\d+)(\s|-)?(\d+)'
        add_phone_pattern = r'Д|доб.?\s?(\d+)'
        phone = contact_info[5]
        if phone:
            ph_numbers = re.sub(phone_pattern, r'\2\3\5\7', phone)
            add_number = re.findall(add_phone_pattern, phone)
            fixed_number = '+7'
            fixed_number += f'({ph_numbers[:3]})'
            fixed_number += f'{ph_numbers[3:6]}-{ph_numbers[6:8]}-{ph_numbers[8:10]}'
            if add_number:
                fixed_number += f' доб.{add_number[0]}'
            contact_info[5] = fixed_number
        return contact_info






if __name__ == '__main__':
    test_phonebook = PhoneBook()
    test_phonebook.generate_contacts(contacts_list[1:])
    for contact in test_phonebook.phonebook_contacts:
        print(contact)
    print('========')
    test_phonebook.find_and_merge_similar()
    for contact in test_phonebook.phonebook_contacts:
        print(contact)
    fixed_contact_list = test_phonebook.get_list()
    print(fixed_contact_list)
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(fixed_contact_list)
