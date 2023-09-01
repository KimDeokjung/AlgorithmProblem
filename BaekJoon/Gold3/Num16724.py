import sys
input = sys.stdin.readline

N, M = map(int, input().split())

inputData = []
totalFlag = [[False for _ in range(1001)] for _ in range(1001)]
result = 0
checkSum = dict()
checkSum["D"] = (1, 0)
checkSum["U"] = (-1, 0)
checkSum["L"] = (0, -1)
checkSum["R"] = (0, 1)

for x in range(N): inputData.append(list(input()))

for x in range(N):
    for y in range(M):
        if inputData[x][y] == "": continue

        nowFlag = set()
        nowX = x
        nowY = y
        while True:
            data = inputData[nowX][nowY]
            nowFlag.add(nowX * 2000 + nowY)
            totalFlag[nowX][nowY] = True
            inputData[nowX][nowY] = ""

            nowX += checkSum[data][0]
            nowY += checkSum[data][1]

            if nowX * 2000 + nowY in nowFlag:
                result += 1
                break
            elif totalFlag[nowX][nowY]:
                break

print(result)
