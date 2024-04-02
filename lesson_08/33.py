# Задача №33. Решение в группах
# Хакер (осуждаю...) Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

quantity_of_as = int(input('Введите кол-во оценок: '))
assessment = list()

for i in range(quantity_of_as):
    x = int(input(f'Введите оценку №{i + 1} из {quantity_of_as}: '))
    assessment.append(x)

min_as = min(assessment)
max_as = max(assessment)

for i in range(len(assessment)):
    if assessment[i] == max_as:
        assessment[i] = min_as

print(*assessment)
