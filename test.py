list_01 = [1, 2, 3, 5, 8, 15, 23, 38]
print(list_01)
list_01 = [i for i in list_01 if i % 2 == 0]
print(list_01)
list_01 = [(i, i * i) for i in list_01]
print(list_01)
