# Задача 18:
#
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.
#
# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random


def random_array(arr_len):
    return [random.randint(1, arr_len) for _ in range(arr_len)]


def check_int_input(number):
    try:
        number = int(number)
        return int(number)
    except ValueError:
        print("Неверные данные")
        return None


n = check_int_input(input("Введите длину массива: "))
if not n:
    exit()

x = check_int_input(input("Введите число, которое нужно поискать: "))
if not x:
    exit()

arr = random_array(n)
print(arr)

tmp_abs_arr = []

for el in arr:
    tmp_abs_arr.append(abs(el - x))

min_abs_values = []

for i in range(0, len(tmp_abs_arr)):
    if tmp_abs_arr[i] == min(tmp_abs_arr):
        min_abs_values.append(arr[i])

print(f'Ближайший к х элемент, наименьший по величине - {min(min_abs_values)}')
