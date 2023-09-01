from collections import deque

def solution(board):
    answer = 0
    startX = startY = endX = endY = 0
    lenX = len(board)
    lenY = len(board[0])

    for index, x in enumerate(board):
        if "R" in x:
            startX = index
            startY = x.index("R")

        if "G" in x:
            endX = index
            endY = x.index("G")

    checkSum = deque()
    checkSum.append((0, startX, startY))
    flag = [[False for _ in range(101)] for _ in range(101)]

    while len(checkSum) != 0:
        totalNum, originX, originY = checkSum.popleft()
        point = [(0, 0), (0, 0), (0, 0), (0, 0)]

        index = 0
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            nowX = originX
            nowY = originY

            while True:
                if 0 <= nowX + x < lenX and 0 <= nowY + y < lenY:
                    if board[nowX + x][nowY + y] == "D":
                        point[index] = (nowX, nowY)
                        break
                    else:
                        nowX += x
                        nowY += y
                        continue
                else:
                    point[index] = (nowX, nowY)
                    break
            index += 1

        for x, y in point:
            if x == endX and y == endY: return totalNum + 1

            if not flag[x][y]:
                flag[x][y] = True
                checkSum.append((totalNum + 1, x, y))

    return -1


board = [".D.R", "....", ".G..", "...D"]

print(solution(board))