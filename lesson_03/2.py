# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# Мой вариан, но с учётом счёта от первого числа Фибоначчи
a = 13
first = 0
second = 1
fibo = 0
count = 1

if a == 0:
    print(1)
elif a == 1:
    print(2, 3)
else:
    while a > fibo:
        first = fibo
        fibo += second
        second = first
        count += 1
        if fibo == a:
            print(count)
            break
    else:
        print(-1)

# Вариант с множественным присваиванием
# n = 8
# fib_1 = 1
# fib_2 = 2
# count = 4

# while fib_2 > n:
#     fib_1, fib_2 = fib_2, fib_1 + fib_2
#     count += 1

# if fib_2 != n:
#     print(-1)
# else:
#     print(count)

# TODO Пример с рекурсией - написать.

