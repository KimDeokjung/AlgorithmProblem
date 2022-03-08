import math

math.factorial(5)
n = int(input())

result = 1
flag = n // 2

for x in range(flag):
    n -= 1

    result += math.factorial(n) // math.factorial(x+1) // math.factorial(n - x - 1)

print(int(result) % 10007)
