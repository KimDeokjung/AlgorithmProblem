n, m = map(int, input().split())
inputData = list()

startX = -1
startY = -1

for x in range(n):
    tmp = list(map(int, input().split()))

    for y in range(m):
        if tmp[y] == 2:
            startX = x
            startY = y
        if tmp[y] == 1:
            tmp[y] = -1

    inputData.append(tmp)

flag = [(startX, startY, 0)]
inputData[startX][startY] = 0

while len(flag) != 0:
    x, y, point = flag.pop(0)

    if x - 1 >= 0 and inputData[x - 1][y] == -1:
        flag.append((x - 1, y, point + 1))
        inputData[x - 1][y] = point + 1

    if y - 1 >= 0 and inputData[x][y - 1] == -1:
        flag.append((x, y - 1, point + 1))
        inputData[x][y - 1] = point + 1

    if x + 1 < n and inputData[x + 1][y] == -1:
        flag.append((x + 1, y, point + 1))
        inputData[x + 1][y] = point + 1

    if y + 1 < m and inputData[x][y + 1] == -1:
        flag.append((x, y + 1, point + 1))
        inputData[x][y + 1] = point + 1

for x in inputData:
    print(*x)