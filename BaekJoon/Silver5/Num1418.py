def abc(num):
    tmp = 2
    result = 1
    while tmp < num:
        if tmp > 100:
            break
        if num % tmp == 0:
            num //= tmp
            result = tmp
        else:
            tmp += 1

    return max(result, num)

N = int(input())
K = int(input())
result = 0

for x in range(1, N + 1):
    a = abc(x)
    if a <= K: result += 1

print(result)
