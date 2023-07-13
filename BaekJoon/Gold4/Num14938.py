import heapq

itemValue = [0]
totalResult = 0

n, m, r = map(int, input().split())
itemValue += list(map(int, input().split()))

inputData = [[-1 for _ in range(n + 1)] for __ in range(n + 1)]

for x in range(r):
    a, b, l = map(int, input().split())
    inputData[a][b] = l
    inputData[b][a] = l

for x in range(1, n + 1):
    checkSum = []
    nowResult = itemValue[x]
    nowCheckSum = [-1 for _ in range(n + 1)]
    nowCheckSum[x] = 0
    visited = 1

    for y in range(1, n + 1):
        if inputData[x][y] == -1: continue

        heapq.heappush(checkSum, (inputData[x][y], y))

    while len(checkSum) != 0 and visited != n:
        w, point = heapq.heappop(checkSum)
        if w > m: break

        if nowCheckSum[point] == -1 or nowCheckSum[point] > w:
            if nowCheckSum[point] == -1:
                visited += 1
                nowResult += itemValue[point]
            nowCheckSum[point] = w

            for y in range(1, n + 1):
                if inputData[point][y] == -1: continue

                heapq.heappush(checkSum, (w + inputData[point][y], y))

    totalResult = max(totalResult, nowResult)

print(totalResult)