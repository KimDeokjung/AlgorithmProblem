from collections import deque

def abc(checkSum, xPoint, yPoint, value):
    tmp = deque()
    checkSum[xPoint][yPoint] = {value}

    for x in range(9):
        if value in checkSum[x][yPoint]:
            checkSum[x][yPoint].remove(value)
            if len(checkSum[x][yPoint]) == 1:
                tmp.append((x, yPoint))
        if value in checkSum[xPoint][x]:
            checkSum[xPoint][x].remove(value)
            if len(checkSum[xPoint][x]) == 1:
                tmp.append((xPoint, x))

    xArea = xPoint // 3
    xArea *= 3
    yArea = yPoint // 3
    yArea *= 3

    for x in range(xArea, xArea + 3):
        for y in range(yArea, yArea + 3):
            if value in checkSum[x][y]:
                checkSum[x][y].remove(value)
                if len(checkSum[x][y]) == 1:
                    tmp.append((x, y))

    checkSum[xPoint][yPoint] = {value}
    return tmp


checkSum = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for _ in range(9)] for __ in range(9)]
flag = deque()

for x in range(9):
    for index, y in enumerate(list(input())):
        if y != "0":
            flag.extend(abc(checkSum, x, index, int(y)))

while len(flag) != 0:
    x, y = flag.popleft()

    flag.extend(abc(checkSum, x, y, checkSum[x][y].pop()))

for x in checkSum:
    for y in x:
        print(*y, end="")
    print()