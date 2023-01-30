def input_mod():
    mode = input('Введите режим работы:\n1 - импорт из справочника\n2 - экспорт в справочник: ')
    return mode


def input_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def view_import (result):
    if isinstance(result, str):
        print(result)
    else:
        print(*result, sep='\n') 


def input_export():
    name = input('Введите фамилию: ')
    surname = input('Введите имя: ')
    sec_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    comment = input('Ведите признак телефона (домашний, рабочий): ')
    return '\n', name, surname, sec_name, phone, comment