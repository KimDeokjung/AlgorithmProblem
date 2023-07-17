from collections import deque

N, M = map(int, input().split())
inputData = []
result = -1

for x in range(N):
    inputData.append(list(map(int,input())))

checkSum = deque([[(0, 0), 1, False]])
visited = set()

while len(checkSum) != 0 and result == -1:
    nowData = checkSum.popleft()
    flag = [(nowData[0][0] + 1, nowData[0][1]), (nowData[0][0] - 1, nowData[0][1]), (nowData[0][0], nowData[0][1] + 1), (nowData[0][0], nowData[0][1] - 1)]

    for xPoint, yPoint in flag:
        if xPoint == N -1 and yPoint == M - 1:
            result = nowData[1] + 1
            break
        if 0 > xPoint or xPoint >= N or 0 > yPoint or yPoint >= M: continue

        visitedPoint = xPoint * 100000 + yPoint * 10 + [0, 1][nowData[2]]
        if nowData[2]:
            if inputData[xPoint][yPoint] == 0 and visitedPoint not in visited:
                checkSum.append([(xPoint, yPoint), nowData[1] + 1, nowData[2]])
                visited.add(visitedPoint)
        else:
            if inputData[xPoint][yPoint] == 0 and visitedPoint not in visited:
                checkSum.append([(xPoint, yPoint), nowData[1] + 1, nowData[2]])
                visited.add(visitedPoint)
            elif inputData[xPoint][yPoint] == 1:
                checkSum.append([(xPoint, yPoint), nowData[1] + 1, True])
                visited.add(visitedPoint)

if N + M == 2:
    print(1)
else:
    print(result)
