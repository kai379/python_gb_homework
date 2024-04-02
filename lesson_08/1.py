# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи.
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        num = fibonacci(num - 1) + fibonacci(num - 2)
    return num


serial_number = int(input('Введите порядковый номер числа: '))
print(f'Число Фибоначчи с порядковым номером {serial_number} = {fibonacci(serial_number)}')
