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


# Функция выбора файла для работы
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
            if data_first[i] == '\n':
                if data_for_search in data_first[i - search_index]:
                    search_result_list.append(''.join(data_first[j:i + 1]))
                    contact_index = i
                j = i + 1
    # Если ничего не найдено
    if not search_result_list:
        print('Контакт не найден.\n'
              '1 - Искать ещё раз\n'
              '2 - Выйти в главное меню')
        var = input('Введите номер пункта меню:')
        while var not in ('1', '2'):
            print('Неправильный ввод!!!')
            var = input('Введите номер пункта меню:')
        if var == '1':
            search_menu_list = search_menu()
            search_index, data_for_search = search_menu_list[0], search_menu_list[1]
            search_in_data_first(data_for_search, search_index)
        elif var == '2':
            print()
    else:
        return [search_result_list, contact_index]


def search_in_data_second(data_for_search: str, search_index: int) -> list[list | int]:
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        search_result_list = []
        contact_index = 0
        # Проход по полученному списку из файла
        for i in range(len(data_second)):
            if data_second[i] == '\n':
                i_list = []
                # Поиск по всем элементам, кроме последнего
                if data_second[i] == '\n':
                    i_list = data_second[i - 1].split(';')
                    if data_for_search in i_list[len(i_list) - search_index]:
                        search_result_list.append(data_second[i - 1])
                        search_result_list[0] += '\n'
                        contact_index = i - 1
    # Если ничего не найдено
    if not search_result_list:
        print('Контакт не найден.\n'
              '1 - Искать ещё раз\n'
              '2 - Выйти в главное меню')
        var = input('Введите номер пункта меню:')
        while var not in ('1', '2'):
            print('Неправильный ввод!!!')
            var = input('Введите номер пункта меню:')
        if var == '1':
            search_menu_list = search_menu()
            search_index, data_for_search = search_menu_list[0], search_menu_list[1]
            search_in_data_second(data_for_search, search_index)
        elif var == '2':
            print()
    else:
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
        print('\n--- Результаты поиска: ---'
              ''.join(search_in_data_first_list[0]))
    # Поиск по data_second_variant
    elif file_var == '2':
        search_in_data_second_return = search_in_data_second(data_for_search, search_index)
        print('\n--- Результаты поиска: ---'
              '\n'.join(search_in_data_second_return[0]))


# Получение двух списков, до необходимого контакта и после, c data_first
def get_the_before_and_after_list_for_first(data_for_search: str, search_index: int):
    search_in_data_first_list = search_in_data_first(data_for_search, search_index)
    search_result_list, contact_index = search_in_data_first_list[0], search_in_data_first_list[1]
    up_list = []
    after_list = []
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data_first = file.readlines()
        for i in range(len(data_first)):
            if i == contact_index:
                up_list.append(data_first[0:contact_index - search_index])
                after_list.append(data_first[i + 1:])
    return [*up_list, *after_list]


# Получение двух списков, до необходимого контакта и после, c data_second
def get_the_before_and_after_list_for_second(data_for_search: str, search_index: int):
    search_in_data_second_list = search_in_data_second(data_for_search, search_index)
    search_result_list, contact_index = search_in_data_second_list[0], search_in_data_second_list[1]
    up_list = []
    after_list = []
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data_second = file.readlines()
        for i in range(len(data_second)):
            if i == contact_index:
                up_list.append(data_second[0:contact_index])
                after_list.append(data_second[contact_index + 2:])
    return [*up_list, *after_list]


# Удаление контакта из файлов
def delete_data():
    var = select_file_for_work('В каком файле произвести удаление?')
    search_menu_list = search_menu()
    search_index, data_for_search = search_menu_list[0], search_menu_list[1]
    # Удаление по первому файлу
    if var == '1':
        result_list = get_the_before_and_after_list_for_first(data_for_search, search_index)
        result_list = list(map(lambda x: ''.join(x), result_list))
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(result_list))
    # Удаление по второму файлу
    elif var == '2':
        result_list = get_the_before_and_after_list_for_second(data_for_search, search_index)
        result_list = list(map(lambda x: ''.join(x), result_list))
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(result_list))


# Изменение данных
def change_data():
    var = select_file_for_work('В каком файле произвести изменение контакта?')
    search_menu_list = search_menu()
    search_index, data_for_search = search_menu_list[0], search_menu_list[1]
    # Изменение контакта в первом файле
    if var == '1':
        search_in_data_first_list = search_in_data_first(data_for_search, search_index)
        contact_data = search_in_data_first_list[0]
        print(
            "Что необходимо изменить в контакте?\n"
            "1 - Имя\n"
            "2 - Фамилию\n"
            "3 - Номер телефона\n"
            "4 - Адрес"
        )

        search_var = input('Введите номер пункта меню:')
        while search_var not in ('1', '2', '3', '4'):
            print('Неправильный ввод!!!')
            search_var = input('Введите номер пункта меню:')

        # Число поправки индекса при поиске по:
        search_index_contact = 0
        text_for_input = ''
        match search_var:
            case '1':
                search_index_contact = 0  # Имени
                text_for_input = 'Имя'
            case '2':
                search_index_contact = 1  # Фамилии
                text_for_input = 'Фамилию'
            case '3':
                search_index_contact = 2  # Номеру телефона
                text_for_input = 'номер телефона'
            case '4':
                search_index_contact = 3  # Адресу
                text_for_input = 'адрес'

        data_for_change = input(f'Введите {text_for_input} для изменения контакта: ')
        # Изменение выбранного контакта
        contact_for_change = contact_data[0].split('\n')
        contact_for_change[search_index_contact] = data_for_change
        contact_for_change = list(''.join('\n'.join(contact_for_change)))
        # Слияние списков до контакта + контакт + после контакта
        up_and_after_list = get_the_before_and_after_list_for_first(data_for_search, search_index)
        up_list, after_list = up_and_after_list[0], up_and_after_list[1]
        result_list = [up_list, contact_for_change, after_list]
        result_list = list(map(lambda x: ''.join(x), result_list))
        # Запись в файл результата
        with open('data_first_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(result_list))
    # Изменение контакта во втором файле
    elif var == '2':
        # Поиск контакта
        search_in_data_second_list = search_in_data_second(data_for_search, search_index)
        contact_data = search_in_data_second_list[0]

        print(
            "Что необходимо изменить в контакте?\n"
            "1 - Имя\n"
            "2 - Фамилию\n"
            "3 - Номер телефона\n"
            "4 - Адрес"
        )

        search_var = input('Введите номер пункта меню:')
        while search_var not in ('1', '2', '3', '4'):
            print('Неправильный ввод!!!')
            search_var = input('Введите номер пункта меню:')

        # Число поправки индекса при поиске по:
        search_index_contact = 0
        text_for_input = ''
        match search_var:
            case '1':
                search_index_contact = 0  # Имени
                text_for_input = 'Имя'
            case '2':
                search_index_contact = 1  # Фамилии
                text_for_input = 'Фамилию'
            case '3':
                search_index_contact = 2  # Номеру телефона
                text_for_input = 'номер телефона'
            case '4':
                search_index_contact = 3  # Адресу
                text_for_input = 'адрес'

        data_for_change = input(f'Введите {text_for_input} для изменения контакта: ')
        # Изменение выбранного контакта
        contact_for_change = contact_data[0].split(';')
        contact_for_change[search_index_contact] = data_for_change
        contact_for_change = list(''.join(';'.join(contact_for_change)))
        # Слияние списков до контакта + контакт + после контакта
        up_and_after_list = get_the_before_and_after_list_for_second(data_for_search, search_index)
        up_list, after_list = up_and_after_list[0], up_and_after_list[1]
        result_list = [up_list, contact_for_change, after_list]
        result_list = list(map(lambda x: ''.join(x), result_list))
        # Запись в файл результата
        with open('data_second_variant.csv', 'w', encoding='utf-8') as file:
            file.writelines(''.join(result_list))
