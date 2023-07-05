import sys
input = sys.stdin.readline

N = int(input())
checkSum = [[[-1, -1] for _ in range(3)] for __ in range(2)]

a, b, c = map(int, input().split())
checkSum[0][0][0] = checkSum[0][0][1] = a
checkSum[0][1][0] = checkSum[0][1][1] = b
checkSum[0][2][0] = checkSum[0][2][1] = c

for x in range(1, N):
    nowData = list(map(int, input().split()))

    for index, y in enumerate(nowData):
        minData = 999999
        maxData = -1

        flag = [1]

        if index == 0 or index == 1: flag.append(0)
        if index == 2 or index == 1: flag.append(2)

        for z in flag:
            minData = min(minData, checkSum[(x + 1) % 2][z][1])
            maxData = max(maxData, checkSum[(x + 1) % 2][z][0])

        checkSum[x % 2][index][1] = minData + y
        checkSum[x % 2][index][0] = maxData + y

minResult = 999999
maxResult = -1

for x in checkSum[(N - 1) % 2]:
    minResult = min(minResult, x[1])
    maxResult = max(maxResult, x[0])

print(maxResult, minResult)