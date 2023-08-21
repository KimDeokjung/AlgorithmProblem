def abc(N, level, nowData, flag, checkSum):
    point = []
    checkData = False
    result = 0
    nowCheck = set()

    for x in range(10):
        if flag[x] == 0:
            checkData = True
        else:
            nowCheck.add(x)

    if level == N:
        if checkData:
            return 0
        return 1

    if nowData != 9: point.append(nowData + 1)
    if nowData != 0: point.append(nowData - 1)

    for x in point:
        checkData = str((level + 1) * 10 + x) + str(nowCheck)
        if (checkData) in checkSum:
            if checkSum[checkData] == 0: continue
            result += checkSum[checkData]
        else:
            flag[x] += 1
            tmp = abc(N, level + 1, x, flag, checkSum)
            flag[x] -= 1
            checkSum[checkData] = tmp
            if tmp == 0: continue
            result += tmp

    result %= 1000000000
    return result

N = int(input())
flag = dict()
checkSum = dict()
nowResult = 0
for x in range(10):
    flag[x] = 0

for x in range(1, 10):
    flag[x] += 1
    nowResult += abc(N, 1, x, flag, checkSum)
    nowResult %= 1000000000
    flag[x] -= 1
print(nowResult)
