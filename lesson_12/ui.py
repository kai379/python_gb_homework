from logger import print_data, delete_data, change_data, search_data, create_data


def interface():
    with open('data_first_variant.csv', 'a', encoding='utf-8'):
        pass
    with open('data_second_variant.csv', 'a', encoding='utf-8'):
        pass

    command = '0'
    while command != '4':
        print(
            "Добрый день! Вы попали на специальный бот справочник. \n"
            "1 - Запись данных\n" 
            "2 - Вывод данных\n"
            "3 - Поиск контакта\n"
            "4 - Выход из программы"
        )

        command = input('Введите номер пункта меню:')

        while command not in ('1', '2', '3', '4'):
            print('Неправильный ввод!!!')
            command = input('Введите номер пункта меню:')

        if command == '1':
            create_data()
        elif command == '2':
            print_data()
        elif command == '3':
            search_data()
        elif command == '4':
            print('До свидания')

