def name_data():
    name = input('Введите ваше имя: ')
    return name


def surname_data():
    surname = input('Введите вашу фамилию: ')
    return surname


def phone_data():
    surname = input('Введите ваш телефон: ')
    return surname


def address_data():
    address = input('Введите ваш адрес: ')
    return address


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    return [name, surname, phone, address]


print(input_data())
