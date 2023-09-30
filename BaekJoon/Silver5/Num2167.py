import sys
input = sys.stdin.readline
N, M = map(int, input().split())
inputData = list()
result = list()

for x in range(N): inputData.append(list(map(int, input().split())))

checkSum = [[0 for _ in range(M + 1)] for __ in range(N + 1)]
for x in range(1, N + 1):
    tmp = 0
    for y in range(1, M + 1):
        tmp += inputData[x - 1][y - 1]
        checkSum[x][y] = tmp + checkSum[x - 1][y]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    tmp = 0

    tmp += checkSum[x][y]
    tmp += checkSum[i - 1][j - 1]
    tmp -= checkSum[i - 1][y]
    tmp -= checkSum[x][j - 1]
    result.append(tmp)

print(*result)