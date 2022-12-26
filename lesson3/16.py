# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.
# Ввод: 5
# Ввод: 1
#
# 1 2 1 2 2
# Вывод: 2

import random


def random_array(arr_len):
    return [random.randint(1, arr_len // 2) for _ in range(arr_len)]


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

x_count = 0
for el in arr:
    if el == x:
        x_count += 1

# Или вот так
# x_count = arr.count(x)


print(f'Количество элементов {x} в массиве = {x_count}')
