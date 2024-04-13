from logger import input_data, print_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник. \n 1 - Запись данных \n 2 - Вывод данных")
    command = int(input('Введите число: '))

    while command != 1 and command != 2:
        print('Неправильный ввод')
        command = int(input('Введите число'))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()





