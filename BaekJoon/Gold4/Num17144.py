import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

inputData = [[[0 for _ in range(C)] for __ in range(R)] for ___ in range(2)]
inputDataFlag = 0
downCleaner = upCleaner = -1
totalResult = 0


for x in range(R):
    for index, y in enumerate(list(map(int, input().split()))):
        inputData[0][x][index] = y
        if y == -1 and upCleaner == -1:
            upCleaner = x
        elif y == -1:
            downCleaner = x
        else:
            totalResult += y

for t in range(T):
    targetFlag = inputDataFlag + 1
    targetFlag %= 2
    for x in range(R):
        for y in range(C):
            if x == 0:
                if y == C - 1:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x + 1][y] - ((inputData[inputDataFlag][x + 1][y] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) +\
                                                  (inputData[inputDataFlag][x + 1][y - 1] // 5) +\
                                                  (inputData[inputDataFlag][x + 2][y] // 5)
                elif y == C - 2:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y + 1] - ((inputData[inputDataFlag][x][y + 1] // 5) * 2)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) +\
                                                  (inputData[inputDataFlag][x + 1][y + 1] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y + 1] - ((inputData[inputDataFlag][x][y + 1] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) +\
                                                  (inputData[inputDataFlag][x][y + 2] // 5) +\
                                                  (inputData[inputDataFlag][x + 1][y + 1] // 5)
            elif x < upCleaner:
                if y == 0:
                    if x == 1:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x - 1][y] - ((inputData[inputDataFlag][x - 1][y] // 5) * 2)) + \
                                                      (inputData[inputDataFlag][x - 1][y + 1] // 5) + \
                                                      (inputData[inputDataFlag][x][y] // 5)
                    else:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x - 1][y] - ((inputData[inputDataFlag][x - 1][y] // 5) * 3)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) +\
                                                      (inputData[inputDataFlag][x - 1][y + 1] // 5) +\
                                                      (inputData[inputDataFlag][x - 2][y] // 5)
                elif y == C - 1:
                    if x == upCleaner:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 4)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) + \
                                                      (inputData[inputDataFlag][x][y - 2] // 5) + \
                                                      (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                      (inputData[inputDataFlag][x + 1][y - 1] // 5)
                    else:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x + 1][y] - ((inputData[inputDataFlag][x + 1][y] // 5) * 3)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) + \
                                                      (inputData[inputDataFlag][x + 1][y - 1] // 5) + \
                                                      (inputData[inputDataFlag][x + 2][y] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y] - ((inputData[inputDataFlag][x][y] // 5) * 4)) + \
                                                  (inputData[inputDataFlag][x + 1][y] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y] // 5) + \
                                                  (inputData[inputDataFlag][x][y + 1] // 5) + \
                                                  (inputData[inputDataFlag][x][y - 1] // 5)
            elif x == upCleaner:
                if y == 0:
                    inputData[targetFlag][x][y] = -1
                    totalResult -= (inputData[inputDataFlag][x - 1][y] - ((inputData[inputDataFlag][x - 1][y] // 5) * 2)) + \
                                                  (inputData[inputDataFlag][x - 2][y] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y + 1] // 5)
                elif y == 1:
                    inputData[targetFlag][x][y] = 0
                elif y == 2:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x + 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y - 1] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 4)) + \
                                                  (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x + 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x][y - 2] // 5)
            elif x == downCleaner:
                if y == 0:
                    inputData[targetFlag][x][y] = -1
                    totalResult -= (inputData[inputDataFlag][x + 1][y] - ((inputData[inputDataFlag][x + 1][y] // 5) * 2)) + \
                                   (inputData[inputDataFlag][x + 2][y] // 5) + \
                                   (inputData[inputDataFlag][x + 1][y + 1] // 5)
                elif y == 1:
                    inputData[targetFlag][x][y] = 0
                elif y == 2:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x + 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y - 1] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 4)) + \
                                                  (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x + 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x][y - 2] // 5)
            elif R - 1 > x > downCleaner:
                if y == 0:
                    if x == R - 2:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x + 1][y] - ((inputData[inputDataFlag][x + 1][y] // 5) * 2)) + \
                                                      (inputData[inputDataFlag][x + 1][y + 1] // 5) + \
                                                      (inputData[inputDataFlag][x][y] // 5)
                    else:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x + 1][y] - ((inputData[inputDataFlag][x + 1][y] // 5) * 3)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) +\
                                                      (inputData[inputDataFlag][x + 1][y + 1] // 5) +\
                                                      (inputData[inputDataFlag][x + 2][y] // 5)
                elif y == C - 1:
                    if x == downCleaner:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y - 1] - ((inputData[inputDataFlag][x][y - 1] // 5) * 4)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) + \
                                                      (inputData[inputDataFlag][x][y - 2] // 5) + \
                                                      (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                      (inputData[inputDataFlag][x + 1][y - 1] // 5)
                    else:
                        inputData[targetFlag][x][y] = (inputData[inputDataFlag][x - 1][y] - ((inputData[inputDataFlag][x - 1][y] // 5) * 3)) + \
                                                      (inputData[inputDataFlag][x][y] // 5) + \
                                                      (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                      (inputData[inputDataFlag][x - 2][y] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y] - ((inputData[inputDataFlag][x][y] // 5) * 4)) + \
                                                  (inputData[inputDataFlag][x + 1][y] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y] // 5) + \
                                                  (inputData[inputDataFlag][x][y + 1] // 5) + \
                                                  (inputData[inputDataFlag][x][y - 1] // 5)
            elif x == R - 1:
                if y == C - 1:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x - 1][y] - ((inputData[inputDataFlag][x - 1][y] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y - 1] // 5) + \
                                                  (inputData[inputDataFlag][x - 2][y] // 5)
                elif y == C - 2:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y + 1] - ((inputData[inputDataFlag][x][y + 1] // 5) * 2)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y + 1] // 5)
                else:
                    inputData[targetFlag][x][y] = (inputData[inputDataFlag][x][y + 1] - ((inputData[inputDataFlag][x][y + 1] // 5) * 3)) + \
                                                  (inputData[inputDataFlag][x][y] // 5) + \
                                                  (inputData[inputDataFlag][x][y + 2] // 5) + \
                                                  (inputData[inputDataFlag][x - 1][y + 1] // 5)
    inputDataFlag += 1
    inputDataFlag %= 2

print(totalResult)