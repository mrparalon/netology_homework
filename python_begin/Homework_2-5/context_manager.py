from time import time, strftime 

class FileTimerOpener():
    def __init__(self, filename, mode='r', encoding='utf8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
    
    def __enter__(self):
        print('Время запуска кода:', strftime('%H:%M:%S'), '\n')
        self.start = time()
        self.opened_file = open(self.filename, self.mode, encoding = self.encoding)
        return self.opened_file

    def __exit__(self, *args):
        self.opened_file.close()
        print('Время завершения кода:', strftime('%H:%M:%S'))
        self.stop = time()
        print(f'Программа завершилась за {self.stop - self.start} сек')

def character_check(line, character_dict):
    for name, counter in character_dict.items():
        if name in line:
            counter += 1
            character_dict[name] = counter
    return character_dict


with FileTimerOpener('Homework_2-5\\voina-i-mir.fb2') as book:
    character_dict = {'Наташ': 0, 'Пьер': 0, 'Андре': 0, 'Анатол': 0}
    pierre_natasha = 0
    for line in book:
        if 'Наташ' in line and 'Пьер' in line:
            pierre_natasha += 1
        character_dict = character_check(line, character_dict)
        
    print(f'Пьер и Наташа упоминаются в одном абзаце {pierre_natasha} раз')
    main_character = max(character_dict, key=character_dict.get)
    print(f'Судя по количеству упоминаний, главный персонаж "Война и Мир" - {main_character} - {character_dict[main_character]} упоминаний\n')
