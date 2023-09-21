import heapq

N = int(input())
inputData = []
checkSum = []
visitedData = dict()
target = (2 ** N) - 1
for x in range(N): inputData.append(list(map(int, input().split())))

flag = 1
point = 1
for x in range(1, N):
    point *= 2
    if inputData[0][x] == 0: continue
    heapq.heappush(checkSum, (inputData[0][x], flag + point, x))

while True:
    value, checkData, lastVisited = heapq.heappop(checkSum)
    originCheckData = checkData
    if checkData == target:
        if inputData[lastVisited][0] != 0:
            heapq.heappush(checkSum, (value + inputData[lastVisited][0], target + 1, 0))
        continue
    elif checkData == target + 1:
        print(value)
        break

    p = 0
    f = 1
    while p < N:
        nowFlag = checkData % 2

        if nowFlag == 1 or inputData[lastVisited][p] == 0 or ((originCheckData + f) * 17 + p in visitedData and (visitedData[(originCheckData + f) * 17 + p] <= value + inputData[lastVisited][p])):
            pass
        else:
            heapq.heappush(checkSum, (value + inputData[lastVisited][p], originCheckData + f, p))
            visitedData[(originCheckData + f) * 17 + p] = value + inputData[lastVisited][p]

        f *= 2
        p += 1
        checkData //= 2



