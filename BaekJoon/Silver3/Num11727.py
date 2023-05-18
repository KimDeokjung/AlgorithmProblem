def CFuntion(n, r):
    result = 1

    for x in range(1, r + 1):
        result *= n - x + 1
        result //= x

    return result

n = int(input())
m = 0

result = 0

while n >= 0:
    checkSum = CFuntion(n + m, m)
    checkSum *= (2 ** m)

    result += checkSum
    result %= 10007

    n -= 2
    m += 1

print(result)

