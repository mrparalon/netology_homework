def calc_pol_notatin(pol_notation_str):
    try:
        pol_notation_list = pol_notation_str.split()
        if len(pol_notation_list) > 3:
            raise IndexError
        first_arg = int(pol_notation_list[1])
        second_arg = int(pol_notation_list[2])
        prefix = pol_notation_list[0]
        assert prefix in ['/','*','-','+']
        if prefix == '+':
            print(first_arg+second_arg)
        if prefix == '-':
            print(first_arg-second_arg)
        if prefix == '*':
            print(first_arg*second_arg)
        if prefix == '/':
            print(first_arg/second_arg)
    except IndexError:
        print("Вы ввели неправильное количество аргументов. В вводе должны быть 3 аргумента, разделенных пробелами")
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print('Вы ввели НЕ число в качестве 2 или 3 аргумента. Вторыми аргументами должны быть числа')
    except AssertionError:
        print("Первый символ не знак операции! Первым символом могут быть + / * -")

print("Это калькулятор, который реализует Польскую нотацию\nВведите выражение вида '+ 2 2'\nвведите stop, чтобы выйти")


while True:
    pol_notation_str = input()
    if pol_notation_str == 'stop':
        break
    calc_pol_notatin(pol_notation_str)
