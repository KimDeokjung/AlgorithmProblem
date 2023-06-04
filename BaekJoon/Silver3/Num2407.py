n, m = map(int, input().split())

result = 1
for x in range(n, n - m, -1):
    result *= x
    result //= (n - x + 1)

print(result)