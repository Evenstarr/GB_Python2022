# Задача 12
#
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import math


def check_number(number):
    is_natural_less_than1k = False
    if 0 < number <= 1000:
        is_natural_less_than1k = True

    return is_natural_less_than1k


try:
    s = int(input("Введите сумму S: "))
except ValueError:
    print("Неверные данные")
    exit()

try:
    p = int(input("Введите произведение P: "))
except ValueError:
    print("Неверные данные")
    exit()

# Тут вычисления типа
# x + y = s, x * y = p. x = s - y.
# (s - y) * y = p. В итоге решаем квадратное уравнение y*2 - s*y + p  = 0

dis = s * s - 4 * 1 * p

if dis < 0:
    print(f'Решения нет')
elif dis == 0:
    solution = s/2
    print(f'Оба числа равны, значение - {int(solution)}')
    if not check_number(solution):
        print(f'Но решение не соответствует условиям натурального числа <=1000')
else:
    solution1 = (s + math.sqrt(dis)) / 2
    solution2 = (s - math.sqrt(dis)) / 2
    print(f'2 числа, значения: {int(solution1)} и {int(solution2)}')
    if not check_number(solution1) or not check_number((solution2)):
        print(f'Но решения не соответствует условиям натурального числа <=1000')
