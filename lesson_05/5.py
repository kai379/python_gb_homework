# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

list_1 = [1, 2, 3, 4, 5, 3]
k = 3

count = 0

for i in list_1:
    if k == i:
        count += 1

print(count)
