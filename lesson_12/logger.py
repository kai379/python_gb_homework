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
        file.write(f"{contact['name']};{contact['surname']};{contact['phone']};{contact['address']}\n")


# Функция добавления контакта в один из файлов
def create_data():
    contact = input_data()
    var = input(f"\nВ каком формате записать данные?\n\n"
                f"1 Вариант: \n"
                f"{contact['name']}\n{contact['surname']}\n{contact['phone']}\n{contact['address']}\n\n"
                f"2 Вариант: \n"
                f"{contact['name']};{contact['surname']};{contact['phone']};{contact['address']}\n"
                f"Выберите номер варианта: ")

    while var != '1' and var != '2':
        print("Неправильный ввод!!!")
        var = input("Введите номер варианта: ")

    if var == '1':
        # with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
        #     file.write(f"{contact['name']}\n{contact['surname']}\n{contact['phone']}\n{contact['address']}\n\n")
        record_contact_in_first_f(contact)
    elif var == '2':
        # with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
        #     file.write(f"{contact['name']};{contact['surname']};{contact['phone']};{contact['address']}\n")
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


def print_data():
    var = select_file_for_work('Из какого файла вывести информацию?')

    if var == '1':
        print('Вывожу данные из 1 файла: \n')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_lists = []
            print(data_first)
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_lists.append(''.join(data_first[j:i + 1]))
                    j = i + 1
                    print(data_first_lists)
            print(data_first_lists)
            print(''.join(data_first_lists))
    elif var == '2':
        print('Вывожу данные из 2 файла: \n')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
            data_second = file.readlines()
            print(*data_second)


def delete_data():
    print()


def change_data():
    print()


def search_data():
    file_var = select_file_for_work('По какому файлу осуществить поиск?')

    # print(
    #     "По каким данным осуществлять поиск\n"
    #     "1 - По имени\n"
    #     "2 - По фамилии\n"
    #     "3 - По номеру телефона\n"
    #     "4 - По адресу"
    # )
    #
    # search_var = input('Введите номер пункта меню:')
    # while search_var not in ('1', '2', '3', '4'):
    #     print('Неправильный ввод!!!')
    #     search_var = input('Введите номер пункта меню:')

    data_for_search = input('Введите Имя, Фамилию, номер телефона или адрес для поиска: ')

    if file_var == '1':  # Поиск по data_first_variant
        with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
            data_first = file.readlines()
            data_first_lists = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_lists.append(''.join(data_first[j:i + 1]))
                    j = i + 1
            search_results = []
            for i in range(len(data_first_lists)):
                if data_for_search in data_first_lists[i]:
                    search_results.append(data_first_lists[i])
            print(*search_results)
    elif file_var == '2':  # Поиск по data_second_variant
        print()
