N, M = map(int, input().split())

inputData = []
result = []

for x in range(1, N + 1):
    rank = int(input())
    inputData.insert(rank - 1, x)

for x in range(M - 1, -1, -1):
    rank = int(input())
    result.insert(rank - 1, inputData[x])

print(*result[:3])