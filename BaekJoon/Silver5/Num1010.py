T = int(input())
result = []

for _ in range(T):
    N, M = map(int, input().split())

    tmp = 1
    for x in range(M, M - N, -1):
        tmp *= x

    for x in range(1, N + 1):
        tmp //= x

    result.append(tmp)

print(*result)