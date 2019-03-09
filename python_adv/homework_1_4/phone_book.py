from pprint import pprint


class Contact:
    def __init__(self, first_name, second_name, phone, favorite=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.phone = phone
        self.favorite = favorite
        self.add_info = kwargs

    def __str__(self):
        fav = 'да' if self.favorite else 'нет'
        add_info = []
        for site, contact in self.add_info.items():
            add_info.append(site + ' : ' + contact)
        add_info_str = '\n\t' + '\n\t'.join(add_info)

        result = f'Имя: {self.first_name}\n'
        result += f'Фамилия: {self.second_name}\n'
        result += f'Телефон: {self.phone}\n'
        result += f'В избранных: {fav}\n'
        result += f'Дополнительная информация:{add_info_str}'
        return result


class PhoneBook:
    def __init__(self, phone_book_name):
        self.phone_book_name = phone_book_name
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.phone] = contact
        print(f'Контакт {contact.first_name} {contact.second_name} добавлен')
    
    def get_all_contacts(self):
        all_contacts = []
        for contact in self.contacts.values():
            print(contact)
            all_contacts.append(contact.__str__())
        return all_contacts


    def del_contact(self, phone):
        if phone in self.contacts:
            deleted_contact = self.contacts.pop(str(phone))
            print(f'{deleted_contact.first_name} {deleted_contact.second_name} удален')
        else:
            print(f'Контакта с телефоном {str(phone)} нет!')
        
    def find_favs(self):
        favs = list(filter(lambda contact: contact.favorite, self.contacts.values()))
        return favs

    def find_by_name(self, first_name, second_name):
        finded_contact = list(filter(lambda contact: contact.first_name.lower() == first_name.lower() and contact.second_name.lower() == second_name.lower(), self.contacts.values()))
        return finded_contact[0]


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    fedor = Contact('Fedor', 'Lebedev', '+71235051231', favorite=True, telegram='@fedor', email='fedor@lebedev.ru')
    test_phone_book = PhoneBook('test')
    test_phone_book.add_contact(jhon)
    test_phone_book.add_contact(fedor)
    
    print('\n_________вывод избранных_________\n'.upper())
    for contact in test_phone_book.find_favs(): print(contact)

    print('\n_________поиск по имени_________\n'.upper())
    print(test_phone_book.find_by_name('Jhon', 'smith'))

    print('\n_________вывод всех контактов_________\n'.upper())
    test_phone_book.get_all_contacts()

    print('\n_________удаление_________'.upper())
    test_phone_book.del_contact('+71234567809')
    test_phone_book.del_contact('+712345609')

    print('\n_________проверка удаления_________\n'.upper())
    test_phone_book.get_all_contacts()
