# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить
# список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# моё решение
# list_01 = [1, 2, 3, 5, 8, 15, 23, 38]
# list_01 = [i for i in list_01 if i % 2 == 0]
# list_01 = [(i, i * i) for i in list_01]
# print(list_01)

# применить функцию для всех элементов коллекции
# и вернуть в список
def select(f, col):
    return [f(x) for x in col]


# поместить в список элемент из коллекции
# если выполнилось условие f(x)
def where(f, col):
    return [x for x in col if f(x)]


list_01 = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, list_01)  # привести все элементы списка к целочисленным
res = where(lambda x: x % 2 == 0, res)
res = select(lambda x: (x, x ** 2), res)
print(res)
