import sys
input = sys.stdin.readline

N, M = map(int, input().split())
inputData = [[0 for _ in range(N)] for __ in range(N)]
flag = 0
result = []

for x in range(N):
    for index, y in enumerate(map(int, input().split())):
        flag += y
        inputData[x][index] = flag

for x in range(M):
    nowResult = 0
    startX, startY, endX, endY = map(int, input().split())
    startX -= 1
    startY -= 1
    endX -= 1
    endY -= 1

    nowResult += inputData[endX][endY]

    if startY != 0:
        for y in range(startX + 1, endX + 1):
            nowResult -= inputData[y][startY - 1]
            nowResult += inputData[y - 1][N - 1]

    if endY != N - 1:
        for y in range(startX, endX):
            nowResult -= inputData[y][N - 1]
            nowResult += inputData[y][endY]

    if startX == startY == 0: pass
    else:
        if startY == 0:
            startY = N - 1
            startX -= 1
        else:
            startY -= 1

        nowResult -= inputData[startX][startY]

    result.append(nowResult)

print(*result)
