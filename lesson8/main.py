# s = input("Введите выражение: ").split()
s = '11 * 30 * 2 - 14  + 5 + 10 * 3 * 10'.split()
# s = '12 - 4 * 2 + 6 / 3'.split()

print(s)


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


while len(s) > 1:
    if '/' in s or '*' in s:
        for i in range(len(s)):
            if s[i] == '/' or s[i] == '*':
                s[i] = calc(int(s[i-1]), int(s[i+1]), s[i])
                s.pop(i-1)
                s.pop(i)
                break
    else:
        for i in range(len(s)):
            if s[i] == '+' or s[i] == '-':
                s[i] = calc(int(s[i-1]), int(s[i+1]), s[i])
                s.pop(i-1)
                s.pop(i)
                break

print(s[0])
