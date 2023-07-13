def abc(xPoint, yPoint):
    inputData[xPoint][yPoint] = -1
    inputData[xPoint + 1][yPoint + 1] = -1
    inputData[xPoint + 1][yPoint - 1] = -1

    inputData[xPoint + 2][yPoint - 2] = -5

N = int(input())
inputDataFlag = []
tmp = 5
for x in range(11):
    inputDataFlag.append(tmp)
    tmp *= 2
    tmp += 1
tmp = N // 3
k = 0
while tmp != 1:
    k += 1
    tmp //= 2

inputData = [[0 for _ in range(inputDataFlag[k])] for __ in range(N)]

inputPoint = [(0, 2)]
pointFlag = 3
for x in range(k):
    tmp = list()
    for xPoint, yPoint in inputPoint:
        tmp.append((xPoint + pointFlag, yPoint))
        tmp.append((xPoint + pointFlag, yPoint + inputDataFlag[x] + 1))
        tmp.append((xPoint, yPoint + (inputDataFlag[x] // 2 + 1)))

    pointFlag *= 2
    inputPoint = tmp

for xPoint, yPoint in inputPoint:
    abc(xPoint, yPoint)

middlePoint = inputDataFlag[k] // 2 + 1
flag = 1
for x in inputData:
    print(" " * (middlePoint - flag), end="")
    flag2 = 0
    for y in range(middlePoint - flag, middlePoint):
        flag2 += x[y]
        if flag2 < 0:
            flag2 += 1
            print("*", end="")
            continue
        else:
            print(" ", end="")
    print(" " * (inputDataFlag[k] - middlePoint))
    middlePoint += 1
    flag += 2

