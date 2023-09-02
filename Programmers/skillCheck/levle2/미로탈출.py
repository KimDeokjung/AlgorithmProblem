from collections import deque

def solution(maps):
    startX = startY = leverX = leverY = exitX = exitY = 0
    lenX = len(maps)
    lenY = len(maps[0])

    for index, x in enumerate(maps):
        if "S" in x:
            startX = index
            startY = x.index("S")
        if "L" in x:
            leverX = index
            leverY = x.index("L")
        if "E" in x:
            exitX = index
            exitY = x.index("E")

    checkSum = deque()
    flag = [[False for _ in range(lenY)] for __ in range(lenX)]
    checkSum.append([startX, startY, 0])
    flag[startX][startY] = True
    result1 = -1

    while True:
        if result1 != -1 or len(checkSum) == 0: break

        x, y, value = checkSum.popleft()

        nowFlag = []
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < lenX and 0 <= y + j < lenY and not flag[x + i][y + j] and maps[x + i][y + j] != "X":
                nowFlag.append([x + i, y + j])

        for i, j in nowFlag:
            if i == leverX and j == leverY:
                result1 = value + 1
                break
            else:
                checkSum.append([i, j, value + 1])
                flag[i][j] = True

    if result1 == -1: return -1

    checkSum = deque()
    flag = [[False for _ in range(lenY)] for __ in range(lenX)]
    checkSum.append([leverX, leverY, 0])
    flag[leverX][leverY] = True
    result2 = -1

    while True:
        if result2 != -1 or len(checkSum) == 0: break

        x, y, value = checkSum.popleft()

        nowFlag = []
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < lenX and 0 <= y + j < lenY and not flag[x + i][y + j] and maps[x + i][y + j] != "X":
                nowFlag.append([x + i, y + j])

        for i, j in nowFlag:
            if i == exitX and j == exitY:
                result2 = value + 1
                break
            else:
                checkSum.append([i, j, value + 1])
                flag[i][j] = True

    if result2 == -1: return -1

    return result1 + result2

print(solution(["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]	))