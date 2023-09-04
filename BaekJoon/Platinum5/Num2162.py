import sys
input = sys.stdin.readline

def abc(x1, y1, x2, y2, targetX):
    if x2 - x1 == 0:
        return y1

    tmp = (y2 - y1) / (x2 - x1)
    tmp2 = y1 - tmp * x1

    return targetX * tmp + tmp2

def findCross(x1, y1, x2, y2, x3, y3, x4, y4):
    if x1 > x2: x1, y1, x2, y2 = x2, y2, x1, y1
    if x3 > x4: x3, y3, x4, y4 = x4, y4, x3, y3

    if x1 > x3: targetX1 = x1
    else: targetX1 = x3

    if x2 < x4: targetX2 = x2
    else: targetX2 = x4

    if targetX1 > targetX2:
        return False
    tmp1, tmp2, tmp3, tmp4 = abc(x1, y1, x2, y2, targetX1), abc(x3, y3, x4, y4, targetX1), abc(x1, y1, x2, y2, targetX2), abc(x3, y3, x4, y4, targetX2)
    flag1 = tmp1 - tmp2
    flag2 = tmp3 - tmp4

    if x2 - x1 == 0:
        if min(y1, y2) <= tmp2 <= max(y1, y2) or min(y1, y2) <= tmp4 <= max(y1, y2):
            return True
        else:
            return False
    elif x4 - x3 == 0:
        if min(y3, y4) <= tmp1 <= max(y3, y4) or min(y3, y4) <= tmp3 <= max(y3, y4):
            return True
        else:
            return False
    elif flag1 * flag2 < 0 or -0.0001 < flag1 < 0.0001 or -0.0001 < flag2 < 0.0001:
        return True
    else:
        return False


def findRoot(flag, data):
    if flag[data] == data:
        return data

    rootA = findRoot(flag, flag[data])
    flag[data] = rootA
    return rootA

def unionRoot(flag, dataA, dataB):
    rootA = findRoot(flag, dataA)
    rootB = findRoot(flag, dataB)

    if rootA < rootB:
        flag[rootB] = rootA
    else:
        flag[rootA] = rootB


N = int(input())
inputData = []
checkSum = []
flag = []

for x in range(N):
    inputData.append(list(map(int, input().split())))
    flag.append(x)

for x in range(N):
    x1, y1, x2, y2 = inputData[x]
    for y in range(x + 1, N):
        x3, y3, x4, y4 = inputData[y]

        if findCross(x1, y1, x2, y2, x3, y3, x4, y4):
            rootA = findRoot(flag, x)
            rootB = findRoot(flag, y)

            if rootA != rootB: unionRoot(flag, rootA, rootB)

resultDict = {}
maxResult = 0

for x in range(N):
    rootA = findRoot(flag, x)
    if rootA in resultDict:
        resultDict[rootA] += 1
        maxResult = max(maxResult, resultDict[rootA])
    else:
        resultDict[rootA] = 1
        maxResult = max(maxResult, 1)

print(len(resultDict))
print(maxResult)
