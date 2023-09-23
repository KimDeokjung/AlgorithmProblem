A, B, N = map(int, input().split())

for _ in range(N):
    A %= B
    A *= 10

result = A / B
print(int(result))
