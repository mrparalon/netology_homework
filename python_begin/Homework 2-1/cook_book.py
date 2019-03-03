from pprint import pprint

def parse_cook_book(file_name):
    cook_book = {}
    with open(file_name) as f:
        f = open(file_name, 'r')
        while True:
            dish_name, products = read_dish(f)
            cook_book[dish_name] = products
            stop_flag = f.readline()
            if not stop_flag:
                break
    return cook_book


def read_dish(file_obj):
    f = file_obj
    dish_name = f.readline().strip()
    products = []
    ingridients = int(f.readline().strip())
    for i in range(ingridients):
        ingrideint_list_view = f.readline().strip().split(' | ')
        ingridient = ingrideint_list_view[0]
        qty = int(ingrideint_list_view[1])
        measure = ingrideint_list_view[2]
        products.append({'ingridient_name': ingridient, 'quantity': qty, 'measure': measure})
    return dish_name, products


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingridient in cook_book[dish]:
                ingridient_name = ingridient['ingridient_name']
                measure = ingridient['measure']
                qty = ingridient['quantity']
                if ingridient_name not in shop_list:
                    shop_list[ingridient_name] = {'mesure': measure, 'quantity': qty*person_count}
                else:
                    shop_list[ingridient_name]['measure'] += qty * person_count
        else: print("Блюда нет в списке рецептов!")
    return shop_list


def print_with_no_globals(file_name, dishes, person_count):
    cook_book = parse_cook_book(file_name)
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    pprint(cook_book)
    pprint(shop_list)

print_with_no_globals('Homework 2-1\\recipe.txt', ['Запеченный картофель', 'Омлет'], 2)

