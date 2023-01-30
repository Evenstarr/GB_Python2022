# m = input("Введите выражение: ").split()
# m = '12 + 15'.split()
# m = '12 + 15 - 4'.split()
m = '12 - 4 * 2 + 6 / 3'.split()

m2 = []


def calc(val1, val2, operation):
    match operation:
        case "+":
            return val1 + val2
        case "-":
            return val1 - val2
        case "*":
            return val1 * val2
        case "/":
            return val1 / val2


mult_arr = []
i = 0
while i < len(m):
    if m[i] == "*" or m[i] == "/":
        result = calc(int(m[i - 1]), int(m[i + 1]), m[i])
        if mult_arr:
            mult_arr.pop()
        mult_arr.append(result)
        i += 1
    else:
        mult_arr.append(m[i])
    i += 1

res = int(mult_arr[0])
for i in range(1, len(mult_arr) - 1, 2):
    res = calc(res, int(mult_arr[i + 1]), mult_arr[i])

print(res)
