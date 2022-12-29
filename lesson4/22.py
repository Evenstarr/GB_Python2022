# Задача 22:
#
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.
# Input: 11 6
#
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)
# Output: 11 6
#
# 6 12

import random


def random_set(length):
    return [random.randint(1, 10) for _ in range(length)]


def check_int_input(number):
    try:
        number = int(number)
        return int(number)
    except ValueError:
        print("Неверные данные")
        return None


n = check_int_input(input("Введите длину первого набора: "))
if not n:
    exit()

m = check_int_input(input("Введите длину второго набора: "))
if not n:
    exit()

n_set = random_set(n)
m_set = random_set(m)

print(n_set)
print(m_set)

n_set = set(n_set)
m_set = set(m_set)

intersection = n_set.intersection(m_set)

print(intersection)
