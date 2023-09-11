import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
inputData = list(map(int, input().split()))
checkSum = dict()
flag = []
data = [0]
result = 0
for _ in range(N):
    checkSum[_] = set()
    flag.append(_)
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    checkSum[a].add(b)
    checkSum[b].add(a)


for x in range(N):
    if flag[x] == -1: continue

    tmp = 0
    tmpData = 0
    nowCheckSum = [x]
    while len(nowCheckSum) != 0:
        point = nowCheckSum.pop(0)
        flag[point] = -1
        tmp += 1
        tmpData += inputData[point]

        for i in checkSum[point]:
            if flag[i] == -1: continue

            flag[i] = -1
            nowCheckSum.append(i)

    data.append((tmp, tmpData))

knapsack = [[0 for _ in range(K + 1)] for __ in range(len(data) + 1)]

for x in range(1, len(data)):
    targetPoint = data[x][0]
    targetValue = data[x][1]

    for y in range(1, K ):
        if y >= targetPoint:
            knapsack[x][y] = max(knapsack[x - 1][y], knapsack[x - 1][y - targetPoint] + targetValue)
        else:
            knapsack[x][y] = knapsack[x - 1][y]
        result = max(result, knapsack[x][y])

print(result)