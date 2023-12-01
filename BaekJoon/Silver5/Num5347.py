import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

result = list()
for _ in range(int(input())):
    a, b = map(int, input().split())
    result.append(lcm(a, b))
print(*result)