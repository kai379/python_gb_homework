# input 5
# output 120

factorial = 1
n = 7
while n > 1:
    factorial *= n
    n -= 1

print(factorial)

# TODO Разобраться с примером
'''Пример вычисления факториала с рекурсией (ChatGPT). Для урока 07.'''
# def factorial(n):
#     # Базовый случай: факториал 0 или 1 равен 1
#     if n == 0 or n == 1:
#         return 1
#     # Рекурсивный случай: n! = n * (n-1)!
#     else:
#         return n * factorial(n - 1)
#
# # Вычисление факториала числа 5
# result = factorial(5)
# print(result)  # Вывод: 120

