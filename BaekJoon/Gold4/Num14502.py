import copy

def abc(nowVirus):

    virusNum = len(virus)
    virusFlag = [False for _ in range(virusNum)]
    result = 0

    for x in range(virusNum):
        if virusFlag[x]: continue
        virusFlag[x] = True
        checkSum = [virus[x]]
        while len(checkSum) != 0:
            result += 1
            v_xPoint, v_yPoint = checkSum.pop(0)

            flag = [(v_xPoint - 1, v_yPoint), (v_xPoint + 1, v_yPoint), (v_xPoint, v_yPoint - 1), (v_xPoint, v_yPoint + 1)]

            for xPoint, yPoint in flag:
                if -1 < xPoint < N and -1 < yPoint < M and inputData[xPoint][yPoint] not in [1, nowVirus]:
                    if inputData[xPoint][yPoint] == 2:
                        tmpPoint = virus.index((xPoint, yPoint))
                        if virusFlag[tmpPoint]: pass
                        else:
                            virusFlag[tmpPoint] = True
                            checkSum.append((xPoint, yPoint))
                    else:
                        inputData[xPoint][yPoint] = nowVirus
                        checkSum.append((xPoint, yPoint))

    return result

N, M = map(int, input().split())

inputData = []
virus = []
result = 0
minVirus = 65

for x in range(N):
    tmp = list(map(int, input().split()))
    for index, y in enumerate(tmp):
        if y == 2: virus.append((x, index))
        if y == 0: result += 1

    inputData.append(tmp)


virusNum = len(virus)
virusValue = 10

for x in range(N * M):
    x_xPoint = x // M
    x_yPoint = x % M
    if inputData[x_xPoint][x_yPoint] in [1, 2]: continue

    for y in range(x + 1, N * M):
        y_xPoint = y // M
        y_yPoint = y % M
        if inputData[y_xPoint][y_yPoint] in [1, 2]: continue

        for z in range(y + 1, N * M):
            z_xPoint = z // M
            z_yPoint = z % M
            if inputData[z_xPoint][z_yPoint] in [1, 2]: continue

            inputData[x_xPoint][x_yPoint] = 1
            inputData[y_xPoint][y_yPoint] = 1
            inputData[z_xPoint][z_yPoint] = 1

            minVirus = min(abc(virusValue), minVirus)
            virusValue += 1

            inputData[x_xPoint][x_yPoint] = 0
            inputData[y_xPoint][y_yPoint] = 0
            inputData[z_xPoint][z_yPoint] = 0

print(max(result - minVirus + len(virus) - 3, 0))