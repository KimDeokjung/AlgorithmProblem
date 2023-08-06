def findA(result, xPoint, yPoint):
    tmp = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    for x in range(9):
        if result[x][yPoint] in tmp:
            tmp.remove(result[x][yPoint])

        if result[xPoint][x] in tmp:
            tmp.remove(result[xPoint][x])

    xArea = xPoint // 3
    xArea *= 3
    yArea = yPoint // 3
    yArea *= 3

    for x in range(xArea, xArea + 3):
        for y in range(yArea, yArea + 3):
            if result[x][y] in tmp:
                tmp.remove(result[x][y])

    return tmp

def abc(result, xPoint, yPoint):
    if result[xPoint][yPoint] != 0:
        tmpX = -1
        tmpY = -1
        tmpFlag = False

        for x in range(9):
            for y in range(9):
                if result[x][y] == 0:
                    tmpX = x
                    tmpY = y
                    tmpFlag = True
                    break
            if tmpFlag:
                break

        if tmpX == tmpY == -1:
            return True
        else:
            checkSum = findA(result, tmpX, tmpY)

            if len(checkSum) == 0:
                return False
            else:
                for x in checkSum:
                    result[tmpX][tmpY] = x
                    nowResult = abc(result, tmpX, tmpY)
                    if nowResult:
                        return nowResult
                    else:
                        result[tmpX][tmpY] = 0
                return False
    else:
        checkSum = findA(result, xPoint, yPoint)

        if len(checkSum) == 0:
            return False
        else:
            for x in checkSum:
                result[xPoint][yPoint] = x
                nowResult = abc(result, xPoint, yPoint)
                if nowResult:
                    return nowResult
                else:
                    result[xPoint][yPoint] = 0
            return False

result = [[0 for i in range(9)] for j in range(9)]

for x in range(9):
    for index, y in enumerate(list(input())):
        if y != "0":
            result[x][index] = int(y)

abc(result, 0, 0)

for x in result:
    for y in x:
        print(y, end="")
    print()