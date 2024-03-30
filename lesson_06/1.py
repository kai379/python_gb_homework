# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

stroke = input('Введите символы через пробел: ').split()
dict_stroke = {}

for i in stroke:
    if i in dict_stroke:
        print(f'{i}_{dict_stroke[i]}', end=' ')
    else:
        print(i, end=' ')
    dict_stroke[i] = dict_stroke.get(i, 0) + 1
