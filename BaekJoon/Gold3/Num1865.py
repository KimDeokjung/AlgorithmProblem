import heapq
import sys
input = sys.stdin.readline

T = int(input())
minNum = -99999
totalResult = []

for ___ in range(T):
    N, M, W = map(int, input().split())
    inputData = [[minNum for _ in range(N + 1)] for __ in range(N + 1)]

    for x in range(M):
        S, E, K = map(int, input().split())
        if inputData[S][E] == minNum:
            inputData[S][E] = K
        else:
            inputData[S][E] = min(inputData[S][E], K)

        if inputData[E][S] == minNum:
            inputData[E][S] = K
        else:
            inputData[E][S] = min(inputData[E][S], K)

    for x in range(W):
        S, E, K = map(int, input().split())
        if inputData[S][E] == minNum:
            inputData[S][E] = -K
        else:
            inputData[S][E] = min(inputData[S][E], -K)

    result = "NO"
    for x in range(1, N + 1):
        flag = [minNum for _ in range(N + 1)]
        flagNum = 0
        checkSum = []

        for y in range(1, N + 1):
            if inputData[x][y] == minNum: continue

            heapq.heappush(checkSum, (inputData[x][y], y))

        maxNum = 0
        while True:
            maxNum += 1
            if len(checkSum) == 0 or (flag[x] != minNum and flag[x] < 0) or maxNum > 3000: break

            v, point = heapq.heappop(checkSum)
            if flagNum >= N: break

            if flag[point] == minNum or flag[point] > v:
                if flag[point] == minNum: flagNum += 1

                flag[point] = v
                for y in range(1, N + 1):
                    if inputData[point][y] == minNum: continue
                    heapq.heappush(checkSum, (v + inputData[point][y], y))

        if flag[x] < 0 and flag[x] != minNum:
            result = "YES"
            break
    totalResult.append(result)

print(*totalResult)

