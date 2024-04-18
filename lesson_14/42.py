# Google Colab
# Задача 42
# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения
# переменной min_population и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

import pandas
df = pandas.read_csv('california_housing_train.csv')
min_population = df['population'].min()
max_households_in_min_population = df[df['population'] == min_population]['households'].max()
# print(max_households_in_min_population)

