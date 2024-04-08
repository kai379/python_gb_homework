# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

values = [1, 23, 42, 'asdfg']
transformed_values = list(map(lambda x: x, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
