from itertools import combinations
import copy

def abc(inputData, checkSum):
    result = 0
    if len(inputData) == 1:
        for x in inputData[0]:
            if x == 1: result += 1
        return result

    flag = []
    tmpInput = copy.deepcopy(inputData)
    tmp = tmpInput.pop(0)
    for index, x in enumerate(tmp):
        if x == 1: flag.append(index)

    for x in range(len(flag) + 1):
        for y in combinations(flag, x):
            pointFlag = []
            for i in range(len(tmpInput)):
                for j in range(len(tmpInput[0])):
                    if ((j + i + 1) in y or (j - i - 1) in y) and tmpInput[i][j] == 1:
                        tmpInput[i][j] = 2
                        pointFlag.append((i, j))
            point = str(tmpInput)
            if point in checkSum:
                result = max(result, checkSum[point] + x)
            else:
                tmp2 = abc(tmpInput, checkSum)
                checkSum[point] = tmp2
                result = max(result, tmp2 + len(y))

            for i, j in pointFlag:
                tmpInput[i][j] = 1
    return result

N = int(input())
blackInput = []
whiteInput = []

for x in range(N):
    tmp = list(map(int, input().split()))
    blackTmp = []
    whiteTmp = []
    for y in range(N):
        if (x + y) % 2 == 0:
            blackTmp.append(tmp[y])
            whiteTmp.append(0)
        else:
            blackTmp.append(0)
            whiteTmp.append(tmp[y])
    blackInput.append(blackTmp)
    whiteInput.append(whiteTmp)

blackCheckSum = dict()
whiteCheckSum = dict()

print(abc(blackInput, blackCheckSum) + abc(whiteInput, whiteCheckSum))
