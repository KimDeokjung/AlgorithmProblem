from collections import deque

def abc(a, b, c, d):

    return (a * (11 ** 3)) + (b * (11 ** 2)) + (c * 11) + d

N, M = map(int, input().split())

inputList = []
redBall = [0, 0]
blueBall = [0, 0]
originGoal = [0, 0]
flag = set()
checkSum = deque()
totalResult = 0
for x in range(N):
    tmp = list(input())
    for y in range(M):
        if tmp[y] == "R":
            redBall = [x, y]
            tmp[y] = "."
        if tmp[y] == "B":
            blueBall = [x, y]
            tmp[y] = "."
        if tmp[y] == "O":
            originGoal = [x, y]
            tmp[y] = "."
    inputList.append(tmp)

flag.add(abc(redBall[0], redBall[1], blueBall[0], blueBall[1]))
checkSum.append([redBall[0], redBall[1], blueBall[0], blueBall[1], 0])
inputList[originGoal[0]][originGoal[1]] = "O"

while len(checkSum) != 0:
    originRX, originRY, originBX, originBY, count = checkSum.popleft()

    for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nowRX = nextRX = originRX
        nowRY = nextRY = originRY
        nowBX = nextBX = originBX
        nowBY = nextBY = originBY
        totalResult = 1
        inputList[originRX][originRY] = "R"
        inputList[originBX][originBY] = "B"

        while True:
            if 0 <= nowRX + x < N and 0 <= nowRY + y < M:
                if inputList[nowRX + x][nowRY + y] == ".":
                    nextRX = nowRX + x
                    nextRY = nowRY + y
                elif nowRX + x == originGoal[0] and nowRY + y == originGoal[1]:
                    nextRX = nowRX + x
                    nextRY = nowRY + y
                    if totalResult != 3:
                        totalResult = 2

            if 0 <= nowBX + x < N and 0 <= nowBY + y < M:
                if inputList[nowBX + x][nowBY + y] == ".":
                    nextBX = nowBX + x
                    nextBY = nowBY + y
                elif nowBX + x == originGoal[0] and nowBY + y == originGoal[1]:
                    nextBX = nowBX + x
                    nextBY = nowBY + y
                    totalResult = 3

            if nowRX == nextRX and nowRY == nextRY and nowBX == nextBX and nowBY == nextBY:
                break

            if nextRX != nowRX or nextRY != nowRY:
                inputList[nextRX][nextRY] = "R"
                if nowRX == originGoal[0] and nowRY == originGoal[1]:
                    inputList[nowRX][nowRY] = "O"
                else:
                    inputList[nowRX][nowRY] = "."

            if nextBX != nowBX or nextBY != nowBY:
                inputList[nextBX][nextBY] = "B"
                if nowBX == originGoal[0] and nowBY == originGoal[1]:
                    inputList[nowBX][nowBY] = "O"
                else:
                    inputList[nowBX][nowBY] = "."

            nowRX = nextRX
            nowRY = nextRY
            nowBX = nextBX
            nowBY = nextBY

        nowTmp = abc(nextRX, nextRY, nextBX, nextBY)
        inputList[nextRX][nextRY] = "."
        inputList[nextBX][nextBY] = "."
        if totalResult == 3: continue

        if totalResult == 2:
            if (count + 1) <= 10:
                print(count + 1)
            else:
                print(-1)
            exit()
        if nowTmp not in flag:
            flag.add(nowTmp)
            checkSum.append([nextRX, nextRY, nextBX, nextBY, count + 1])
print(-1)