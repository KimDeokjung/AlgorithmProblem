import copy

inputData = input()
inputData = "!" + inputData
inputDataLen = len(inputData)
bomb = input()
bombLen = len(bomb)
bombCheck = dict()
checkSum = [[] for _ in range(inputDataLen)]
checkSum2 = [False for _ in range(inputDataLen)]

for index, x in enumerate(inputData):
    if index == 0: continue

    tmp = []
    flag = False
    masterFlag = False
    bombWin = False
    point = -1

    for y in checkSum[index - 1][::-1]:
        if masterFlag:
            tmp.insert(0, (y[0], y[1]))
            continue

        if bomb[y[1]] != x and not flag:
            pass
        elif bomb[y[1]] != x:
            masterFlag = True
            tmp.insert(0, (y[0], y[1]))
        elif bomb[y[1]] == x:
            flag = True
            if y[1] + 1 == bombLen:
                bombWin = True
                point = y[0]
                masterFlag = True
            else:
                tmp.insert(0, (y[0], y[1] + 1))

    if bombWin:
        checkSum2[bombCheck[point]] = True
        checkSum[index] = copy.deepcopy(checkSum[bombCheck[point] - 1])
    else:
        if x == bomb[0]:
            if len(tmp) == 0:
                tmp = copy.deepcopy(checkSum[index - 1])
            tmp.append((len(tmp), 1))
            bombCheck[len(tmp) - 1] = index
        checkSum[index] = tmp

result = ""
checkLen = 0
for x in range(1, inputDataLen):
    if checkSum2[x]:
        checkLen += (bombLen - 1)
        continue

    if checkLen == 0:
        result += inputData[x]
    else:
        checkLen -= 1


if result == "":
    print("FRULA")
else:
    print(result)