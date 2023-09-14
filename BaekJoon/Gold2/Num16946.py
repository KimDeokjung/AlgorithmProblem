N, M = map(int, input().split())
flag = [[False for _ in range(M)] for __ in range(N)]
inputData = []
outPutData = [[0 for _ in range(M)] for __ in range(N)]
checkSum = dict()
resultData = []
point = 1

for x in range(N): inputData.append(list(input()))

for x in range(N):
    for y in range(M):
        if inputData[x][y] == "1":
            resultData.append((x, y))
            continue
        elif flag[x][y]:
            continue
        else:
            tmp = [(x, y)]
            count = 0

            while len(tmp) != 0:
                i, j = tmp.pop(0)
                count += 1
                flag[i][j] = True
                inputData[i][j] = point

                for flagX, flagY in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if 0 <= i + flagX < N and 0 <= j + flagY < M and not flag[i + flagX][j + flagY] and inputData[i + flagX][j + flagY] == "0":
                        flag[i + flagX][j + flagY] = True
                        tmp.append((i + flagX, j + flagY))
            checkSum[point] = count
            point += 1

for x, y in resultData:
    tmp = set()
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nowX = x + i
        nowY = y + j
        if 0 <= nowX < N and 0 <= nowY < M and inputData[nowX][nowY] != "1":
            tmp.add(inputData[nowX][nowY])

    nowResult = 1
    for i in tmp:
        nowResult += checkSum[i]

    outPutData[x][y] = nowResult % 10


for x in outPutData:
    for y in x:
        print(y, end="")
    print()