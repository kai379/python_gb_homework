# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

list_01 = [1, 2, 3, 4, 5, 6, 7]
k = int(input('Введите число: '))
list_res = []

k = k % len(list_01)

for i in range(len(list_01) - k):
    list_res.append(list_01[i + k])
print(list_res)

for i in range(k):
    list_res.append(list_01[i])
print(list_res)
