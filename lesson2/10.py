# Задача 10
#
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
#
# 5 -> 1 0 1 1 0
# 2
import random


def random_array(arr_len):
    return [random.randint(0, 1) for _ in range(arr_len)]


try:
    n = int(input("Введите число монеток: "))
    arr = random_array(n)

    print(arr)

    # Вообще тут все сводится к нахождению минимума между количеством 0
    # и количеством 1 в массиве. То есть, min(arr.count(0), arr.count(1)).
    # На случай, если вы хотите другое решение, а не стандартными средствами, решение ниже

    zero_count = 0
    for i in range(n):
        if arr[i] == 0:
            zero_count += 1

    print(f'{zero_count if n - zero_count > zero_count else n - zero_count}')


except ValueError:
    print("Неверные данные")
    exit()


