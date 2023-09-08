from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
flag = [0 for _ in range(N + 1)]
checkSum = dict()
result = []
for x in range(1, N + 1):
    checkSum[x] = []

for x in range(M):
    inputData = list(map(int, input().split()))
    for y in range(1, len(inputData) - 1):
        flag[inputData[y + 1]] += 1
        checkSum[inputData[y]].append(inputData[y + 1])

zeroData = deque()
for x in range(1, N + 1):
    if flag[x] == 0: zeroData.append(x)

while len(zeroData) != 0:
    data = zeroData.popleft()
    result.append(data)

    for x in checkSum[data]:
        flag[x] -= 1
        if flag[x] == 0: zeroData.append(x)

if len(result) != N:
    print(0)
else:
    print(*result)