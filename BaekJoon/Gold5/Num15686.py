from itertools import combinations

N, M = map(int, input().split())
checkSum = []
chicken = []
result = 9999999

for x in range(N):
    tmp = list(map(int, input().split()))

    for index, y in enumerate(tmp):
        if y == 1:
            checkSum.append([x, index, -1])
        elif y == 2:
            chicken.append([x, index])

for x in combinations(chicken, M):
    nowResult = 0

    for y in x:
        for z in range(len(checkSum)):
            tmp = abs(y[0] - checkSum[z][0]) + abs(y[1] - checkSum[z][1])

            if checkSum[z][2] == -1 or checkSum[z][2] > tmp:
                checkSum[z][2] = tmp

    for z in checkSum:
        nowResult += z[2]

    for y in range(len(checkSum)):
        checkSum[y][2] = -1

    result = min(result, nowResult)

print(result)



