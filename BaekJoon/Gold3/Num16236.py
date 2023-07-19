from collections import deque

N = int(input())
inputData = []
sharkX = -1
sharkY = -1
sharkNum = [2, 0]
result = 0

for x in range(N):
    tmp = list(map(int, input().split()))
    for index, y in enumerate(tmp):
        if y == 9:
            sharkX = x
            sharkY = index

    inputData.append(tmp)

inputData[sharkX][sharkY] = 0

while True:
    checkSum = deque()
    checkSum.append((sharkX, sharkY, 0))
    hunt = False
    flag = set()
    huntXP = huntYP = huntNum = -1

    while True:
        if len(checkSum) == 0: break

        xPoint, yPoint, num = checkSum.popleft()

        if -1 < huntNum < num: break

        for x, y in [(xPoint + 1, yPoint), (xPoint, yPoint - 1), (xPoint, yPoint + 1), (xPoint - 1, yPoint)]:
            if -1 < x < N and -1 < y < N and (x * 100 + y) not in flag:
                if inputData[x][y] > sharkNum[0]: continue

                if 0 < inputData[x][y] < sharkNum[0]:
                    hunt = True
                    if huntNum == -1:
                        huntXP = x
                        huntYP = y
                        huntNum = num
                    else:
                        if huntXP > x:
                            huntXP = x
                            huntYP = y
                        elif huntXP == x:
                            if huntYP > y:
                                huntXP = x
                                huntYP = y
                        huntNum = num
                else:
                    flag.add(x * 100 + y)
                    checkSum.append((x, y, num + 1))

    if not hunt:
        break
    else:
        sharkX = huntXP
        sharkY = huntYP
        inputData[sharkX][sharkY] = 0
        result += (huntNum + 1)

        if sharkNum[1] == sharkNum[0] - 1:
            sharkNum[0] += 1
            sharkNum[1] = 0
        else:
            sharkNum[1] += 1

print(result)