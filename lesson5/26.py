# Задача 26:
#
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


if b < 0:
    print(1 / power(a, -b))
elif b >= 0:
    print(power(a, b))
