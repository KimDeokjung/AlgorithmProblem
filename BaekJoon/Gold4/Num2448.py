def abc(xPoint, yPoint):
    inputData[xPoint][yPoint] = True
    inputData[xPoint + 1][yPoint + 1] = True

    inputData[xPoint + 1][yPoint - 1] = True
    inputData[xPoint + 1][yPoint + 1] = True

    inputData[xPoint + 2][yPoint - 2] = True
    inputData[xPoint + 2][yPoint - 1] = True
    inputData[xPoint + 2][yPoint] = True
    inputData[xPoint + 2][yPoint + 1] = True
    inputData[xPoint + 2][yPoint + 2] = True

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

inputData = [[False for _ in range(inputDataFlag[k])] for __ in range(N)]

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

for x in inputData:
    for y in x:
        if y: print("*", end = "")
        else: print(" ", end = "")
    print()
