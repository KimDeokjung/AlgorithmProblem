import sys
input = sys.stdin.readline
N = int(input())
inputData = []
checkSum = [[0 for _ in range(N)] for __ in range(N)]
for x in range(N): inputData.append(list(map(int, input().split())))

for x in range(N - 1):
    for y in range(N - 1 - x):
        z = y + x + 1
        checkSum[y][z] = 2 ** 31
        for k in range(y, z):
            checkSum[y][z] = min(checkSum[y][z], checkSum[y][k] + checkSum[k + 1][z] + inputData[y][0] * inputData[k][1] * inputData[z][1])

print(checkSum[0][-1])