def abc(flag, depth, xPoint, yPoint, sumData):
    checkSum = list()
    result = 0

    if xPoint - 1 >= 0 and (xPoint * 1000 + yPoint - 1000) not in flag: checkSum.append((xPoint - 1, yPoint))
    if yPoint - 1 >= 0 and (xPoint * 1000 + yPoint - 1) not in flag: checkSum.append((xPoint, yPoint - 1))
    if xPoint + 1 < N and (xPoint * 1000 + yPoint + 1000) not in flag: checkSum.append((xPoint + 1, yPoint))
    if yPoint + 1 < M and (xPoint * 1000 + yPoint + 1) not in flag: checkSum.append((xPoint, yPoint + 1))

    if depth == 3:
        popData = flag[1]
        x, y = popData // 1000, popData % 1000
        if x - 1 >= 0 and (x * 1000 + y - 1000) not in flag: checkSum.append((x - 1, y))
        if y - 1 >= 0 and (x * 1000 + y - 1) not in flag: checkSum.append((x, y - 1))
        if x + 1 < N and (x * 1000 + y + 1000) not in flag: checkSum.append((x + 1, y))
        if y + 1 < M and (x * 1000 + y + 1) not in flag: checkSum.append((x, y + 1))

        for x, y in checkSum: result = max(sumData + inputData[x][y], result)
        return result
    else:
        for x, y in checkSum:
            result = max(abc(flag + [x * 1000 + y], depth + 1, x, y, sumData + inputData[x][y]), result)
        return result

N, M = map(int, input().split())
result = 0
inputData = list()

for x in range(N):
    inputData.append(list(map(int, input().split())))

for x in range(N):
    for y in range(M):
        flag = list()
        flag.append(x * 1000 + y)
        result = max(result, abc(flag, 1, x, y, inputData[x][y]))

print(result)
