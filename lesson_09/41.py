# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
# Ввод: 5     1 2 3 4 5     Вывод: 0
# Ввод: 5     1 5 1 5 1     Вывод: 2

n = int(input('Введите длину массива: '))
list_01 = list()
for i in range(n):
    list_01.append(int(input(f'Введите {i} элемент массива: ')))
count = 0
for i in range(1, len(list_01) - 1):
    if list_01[i] > list_01[i - 1] and list_01[i] > list_01[i + 1]:
        count += 1
print(count)
