# Задача 30: Заполните массив элементами арифметической прогрессии.
# (в тесте никакого массива не надо, просто вывести через принт каждое значение с новой строки).
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки. (PS input() не надо)
# Ввод: 7 2 5
# Вывод:
# 7
# 9
# 11
# 13
# 15

a1 = 7
d = 2
n = 5

for i in range(n):
    print(a1 + i * d)
