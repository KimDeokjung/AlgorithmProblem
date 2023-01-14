N = input()

result = 0
num = ""
tmp = 0

for x in N[::-1]:
    if x == "-":
        tmp += int(num)
        result -= tmp
        tmp = 0
        num = ""
    elif x == "+":
        tmp += int(num)
        num = ""
    else:
        num = x + num

result += tmp
result += int(num)

print(result)
