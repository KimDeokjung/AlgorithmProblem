totalResult = []
for _ in range(int(input())):
    n = int(input())
    inputData = list()
    inputData.append(list(map(int, input().split())))
    inputData.append(list(map(int, input().split())))
    result = 0

    for x in range(2):
        for y in range(n):
            if inputData[x][y] == -1: continue

            while True:
                tmpX = x
                tmpY = y

                while True:
                    if inputData[tmpX][tmpY] == -1:break
                    flag = []
                    if tmpX - 1 >= 0: flag.append((tmpX - 1, tmpY))
                    if tmpX + 1 < 2: flag.append((tmpX + 1, tmpY))
                    if tmpY - 1 >= 0: flag.append((tmpX, tmpY - 1))
                    if tmpY + 1 < n: flag.append((tmpX, tmpY + 1))

                    maxData = inputData[tmpX][tmpY]
                    maxX = tmpX
                    maxY = tmpY

                    maxCheckSum = -1
                    for i, j in flag:
                        if maxData != inputData[i][j] and maxCheckSum < inputData[i][j]:
                            maxCheckSum = inputData[i][j]

                    for i, j in flag:
                        if inputData[i][j] > maxData:
                            maxData = inputData[i][j]
                            maxX = i
                            maxY = j
                        elif inputData[i][j] == maxData:
                            flag2 = []
                            if i - 1 >= 0: flag2.append((i - 1, j))
                            if i + 1 < 2: flag2.append((i + 1, j))
                            if j - 1 >= 0: flag2.append((i, j - 1))
                            if j + 1 < n: flag2.append((i, j + 1))

                            maxCheckSum2 = -1
                            for k, l in flag2:
                                if maxData != inputData[k][l] and maxCheckSum2 < inputData[k][l]:
                                    maxCheckSum2 = inputData[k][l]
                            if maxCheckSum2 < maxCheckSum:
                                maxX = i
                                maxY = j

                    if maxData == inputData[tmpX][tmpY] and maxX == tmpX and maxY == tmpY:
                        for i, j in flag:
                            inputData[i][j] = -1

                        result += inputData[tmpX][tmpY]
                        inputData[tmpX][tmpY] = -1
                        break
                    else:
                        tmpX = maxX
                        tmpY = maxY
                if tmpX == x and tmpY == y:
                    break

    totalResult.append(result)

print(*totalResult)