from data_create import name_data, surname_data, phone_data, address_data


# Функция получения данных контакта в виде словаря
def input_data() -> dict:
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    return {'name': name, 'surname': surname, 'phone': phone, 'address': address}
    # Добавил словарь, чтобы разделить большую функцию с урока
    # и при вызове в других функциях брать значения по понятным ключам, а не по индексам кортежей или списков


def record_contact_in_first_f(contact: dict):
    with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f"{contact['name']}\n{contact['surname']}\n{contact['phone']}\n{contact['address']}\n\n")


def record_contact_in_second_f(contact: dict):
    with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
        file.write(f"{contact['name']};{contact['surname']};{contact['phone']};{contact['address']}\n\n")


# Функция добавления контакта в один из файлов
def create_data():
    contact = input_data()
    var = input(f"\nВ какой файл записать данные?\n\n"
                f"1. data_first_variant.csv: \n"
                f"{contact['name']}\n{contact['surname']}\n{contact['phone']}\n{contact['address']}\n\n"
                f"2 data_second_variant.csv: \n"
                f"{contact['name']};{contact['surname']};{contact['phone']};{contact['address']}\n"
                f"Выберите номер варианта: ")

    while var != '1' and var != '2':
        print("Неправильный ввод!!!")
        var = input("Введите номер варианта: ")

    if var == '1':
        record_contact_in_first_f(contact)
    elif var == '2':
        record_contact_in_second_f(contact)


# Функция выбора файла для поиска/записи
def select_file_for_work(menu_text: str) -> str:
    var = input(
        f'{menu_text}\n'
        '1. data_first_variant\n'
        '2. data_second_variant\n'
        'Введите номер файла: '
    )
    while var != '1' and var != '2':
        print("Неправильный ввод!!!")
        var = input("Введите номер варианта: ")
    return var


# Вывод информации из файлов
def print_data():
    var = select_file_for_work('Из какого файла вывести информацию?')

    if var == '1':
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_lists = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_lists.append(''.join(data_first[j:i + 1]))
                    j = i + 1
            print(''.join(data_first_lists))
    elif var == '2':
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            print(*data_second)


def change_data():
    print()


# Меню для режима поиска с возвратом [поправочного индекса (int), данных для поиска (str)]
def search_menu() -> list[int | str]:
    print(
        "По каким данным осуществлять поиск?\n"
        "1 - По имени\n"
        "2 - По фамилии\n"
        "3 - По номеру телефона\n"
        "4 - По адресу"
    )

    search_var = input('Введите номер пункта меню:')
    while search_var not in ('1', '2', '3', '4'):
        print('Неправильный ввод!!!')
        search_var = input('Введите номер пункта меню:')

    # Число поправки индекса при поиске по:
    search_index = 0
    text_for_input = ''
    match search_var:
        case '1':
            search_index = 4  # Имени
            text_for_input = 'Имя'
        case '2':
            search_index = 3  # Фамилии
            text_for_input = 'Фамилию'
        case '3':
            search_index = 2  # Номеру телефона
            text_for_input = 'номер телефона'
        case '4':
            search_index = 1  # Адресу
            text_for_input = 'адрес'

    data_for_search = input(f'Введите {text_for_input} для поиска: ')
    return [search_index, data_for_search]


# Поиск по data_first. Возвращает список со строкой контакта
def search_in_data_first(data_for_search: str, search_index: int) -> list[list | int]:
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        search_result_list = []
        j = 0
        contact_index = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n':  # or i == len(data_first) - 1:
                if data_for_search in data_first[i - search_index]:
                    search_result_list.append(''.join(data_first[j:i + 1]))
                    contact_index = i
                j = i + 1

    return [search_result_list, contact_index]


def search_in_data_second(data_for_search: str, search_index: int) -> list[list | int]:
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        search_result_list = []
        contact_index = 0
        # print('data_second: ', data_second)
        # Проход по полученному списку из файла
        for i in range(len(data_second)):
            if data_second[i] == '\n' or i == len(data_second) - 1:
                i_list = []
                # Поиск по всем элементам, кроме последнего
                if data_second[i] == '\n':
                    i_list = data_second[i - 1].split(';')
                    # print('При /n: ', i_list)
                    if data_for_search in i_list[len(i_list) - search_index]:
                        search_result_list.append(data_second[i - 1])
                        contact_index = i - 1
                # Поиск по последнему элементу
                # elif i == len(data_second) - 1:
                #     i_list = data_second[i].split(';')
                #     # print('При -1: ', i_list)
                #     if data_for_search in i_list[len(i_list) - search_index]:
                #         search_result_list.append(data_second[i])
    return [search_result_list, contact_index]


# Поиск по двум файлам с выводом результата в терминал
def search_data():
    # Выбор файла для работы
    file_var = select_file_for_work('По какому файлу осуществить поиск?')
    # Получение поправочного индекса и данных для поиска
    search_menu_list = search_menu()
    search_index, data_for_search = search_menu_list[0], search_menu_list[1]

    # Поиск по data_first_variant
    if file_var == '1':
        search_in_data_first_list = search_in_data_first(data_for_search, search_index)
        print(''.join(search_in_data_first_list[0]))
    # Поиск по data_second_variant
    elif file_var == '2':
        search_in_data_second_return = search_in_data_second(data_for_search, search_index)
        print('\n--- Результаты поиска: ---'
              '\n'.join(search_in_data_second_return[0]))


def delete_data():
    var = select_file_for_work('В каком файле произвести удаление?')
    search_menu_list = search_menu()
    search_index, data_for_search = search_menu_list[0], search_menu_list[1]
    if var == '1':
        search_in_data_first_list = search_in_data_first(data_for_search, search_index)
        search_result_list, contact_index = search_in_data_first_list[0], search_in_data_first_list[1]
        # list_to_contact = []
        # list_after_contact = []
        result_list = []
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            j = 0
            for i in range(len(data_first)):
                if i == contact_index:
                    result_list.append(data_first[j:contact_index - search_index])
                    result_list.append(data_first[i + 1:])
        result_list = list(map(lambda x: ''.join(x), result_list))
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(result_list))

    elif var == '2':
        search_in_data_second_list = search_in_data_second(data_for_search, search_index)


delete_data()
