import sys
input = sys.stdin.readline

N = int(input())
inputData = list(map(int, input().split()))
M = int(input())
checkSum = [[0 for _ in range(N)] for __ in range(N)]
result = []

for x in range(N):
    checkSum[0][x] = 1

if N >= 2:
    for x in range(N - 1):
        if inputData[x] == inputData[x + 1]:
            checkSum[1][x] = 1

for x in range(2, N):
    for y in range(N - x):
        if checkSum[x - 2][y + 1] == 1 and inputData[y] == inputData[y + x]:
            checkSum[x][y] = 1

for x in range(M):
    S, E = map(int, input().split())
    result.append(checkSum[E - S][S - 1])

print(*result)
