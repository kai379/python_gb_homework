# На столе лежат n монеток. Некоторые из монеток лежат вверх решкой,
# а некоторые – гербом. Ваша задача - определить минимальное количество монеток,
# которые нужно перевернуть, чтобы все монетки лежали одной и той же стороной вверх.

coins = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

zero = 0
one = 0
turn_over = 0

for i in coins:
    if i == 0:
        zero += 1
    else:
        one += 1

if zero > one:
    turn_over = one
else:
    turn_over = zero

print(turn_over)
