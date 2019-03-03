documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "666"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def shelf_handle(command):
    """
    Main function. Gets command from user input, return function from dict. Function defined bellow.

    Command input in while loop in the end of file.
    """

    command_dict = {'p': check_people, 'l': show_list, 's': find_shelf, 'a': add_document, 'd': delete_doc, 'm': move_doc, 'as': add_shelf, 'an': show_all_names}
    return command_dict[command]()


# ЗАДАНИЕ 1

def check_people():
    number = input("Введите номер документа: ")
    for document in documents:
        if document['number'] == number:
            return print("Документ {} принадлежит {}".format(number, document['name']))
    return print("Такого документа нет!")


def show_list():
    for document in documents:
        print('{} "{}" "{}"'.format(document["type"], document["number"], document["name"]))


def find_shelf():
    number = input("Введите номер документа: ")
    for shelf, docs in directories.items():
        if number in docs:
            return print("Докумет {} находится на полке {}".format(number, shelf))
    return print("Нет такого документа!")


def add_document():
    number = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    name = input('Введите имя владельца: ')
    shelf_number = input('Введите номер полки: ')
    documents.append({"type": doc_type, "number": number, "name": name})
    while True:
        if shelf_number in directories.keys():
            directories[shelf_number].append(number)
            return print('Документ добавлен!')
        else:
            print("Такой полки нет! Есть полки: {}".format([x for x in directories.keys()]))
            shelf_number = input("Введите новую полку: ")


def delete_doc():
    number = input("Введите номер документа: ")
    for document in documents:
        if document['number'] == number:
            documents.remove(document)
    for shelf, doc in directories.items():
        if number in doc:
            key_for_del = shelf
    directories[key_for_del].remove(number)
    return print('Документ удален!')

def move_doc():
    number = input("Введите номер документа: ")
    shelf_to_move = input("Введите номер полки, на которую переместиться документ: ")
    for shelf, doc in directories.items():
        if number in doc:
            key_for_del = shelf
            print(shelf, number)
    directories[key_for_del].remove(number)
    directories[shelf_to_move].append(number)


def add_shelf():
    shelf = input('Введите номер полки, которую нужно создать: ')
    directories.setdefault(shelf, [])

def show_all_names():
    for doc in documents:
        try:
            print(doc['name'])
        except KeyError:
            print("В документе {} не указано имя!".format(doc['number']))

command = True

while command:
    command = input("Введите команду: ")
    try:
        shelf_handle(command)
    except KeyError:
        print("Нет такой команды!")
