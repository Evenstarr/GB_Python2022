# Задача 24:
#
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.
# Input: 4
#
# (значения сгенерированы случайным образом
# 4 2 3 1 )
# Output: 9

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


n = check_int_input(input("Введите количество кустов на грядке: "))
if not n:
    exit()

n_set = random_set(n)
print(n_set)

tmp_beginning = 0
tmp_end = 3
sum_tmp = 0

i = 0

while tmp_end <= n:
    tmp_slice = n_set[tmp_beginning:tmp_end]
    if sum(tmp_slice) > sum_tmp:
        sum_tmp = sum(tmp_slice)
    tmp_beginning += 1
    tmp_end += 1

add_sum1 = add_sum2 = 0

if n % 3 != 0:
    add_sum1 = sum(n_set[n-2:n]) + n_set[0]
    add_sum2 = n_set[n-1] + n_set[0] + n_set[1]

print(max(sum_tmp, add_sum1, add_sum2))
