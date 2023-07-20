from collections import deque

inputData = deque()
N = int(input())
startPx = 100001
startPy = 200001
result = 0

for x in range(N):
    tmpX, tmpY = map(int, input().split())
    tmpY += 100000

    if tmpX < startPx:
        startPx = tmpX
        startPy = tmpY
    elif tmpX == startPx and startPy > tmpY:
        startPy = tmpY

    inputData.append((tmpX, tmpY))

while inputData[0][0] != startPx or inputData[0][1] != startPy:
    inputData.append(inputData.popleft())

x1, y1 = inputData.popleft()
inputData.append((x1, y1))

while True:
    if len(inputData) == 0: break

    x2, y2 = inputData.popleft()

    if x1 == x2:
        x1, y1 = x2, y2
        continue
    else:
        tmp = 0
        minY = min(y1, y2)
        maxY = max(y1, y2)

        tmp += (x2 - x1) * minY
        tmp += (x2 - x1) * (maxY - minY) / 2

        result += tmp

    x1, y1 = x2, y2

print(abs(round(result, 1)))