# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

""" Мой вариант """
some_numb = int(input('Введите число: '))
count = 0
for i in range(some_numb + 1):
    if i > 0 and some_numb % i == 0:
        count += 1

if count > 2:
    print('No')
else:
    print('Yes')

""" Вариант с урока """
# flag = True
# i = 2
# while i < some_numb and flag:
#     if some_numb % i == 0:
#         flag = False
#     i += 1
#
# if flag:
#     print('Yes')
# else:
#     print('No')
