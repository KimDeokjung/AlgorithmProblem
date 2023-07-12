import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

frontMap = []
frontFlag = [-1 for _ in range(N + 1)]
frontNum = 1
frontFlag[X] = 0
frontCheckSum = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]
backMap = []
backFlag = [-1 for _ in range(N + 1)]
backNum = 1
backFlag[X] = 0
backCheckSum = [[-1 for _ in range(N + 1)] for ___ in range(N + 1)]

for x in range(M):
    i, j, w = map(int, input().split())
    frontCheckSum[i][j] = w
    backCheckSum[j][i] = w

    if i == X:
        heapq.heappush(frontMap, (w, j))
    if j == X:
        heapq.heappush(backMap, (w, i))


while len(frontMap) != 0 and frontNum != N:
    w, i = heapq.heappop(frontMap)

    if frontFlag[i] == -1 or frontFlag[i] > w:
        if frontFlag[i] == -1:
            frontNum += 1

        frontFlag[i] = w
        for x in range(1, N + 1):
            if frontCheckSum[i][x] == -1: continue
            heapq.heappush(frontMap, (w + frontCheckSum[i][x], x))

while len(backMap) != 0 and backNum != N:
    w, i = heapq.heappop(backMap)

    if backFlag[i] == -1 or backFlag[i] > w:
        if backFlag[i] == -1:
            backNum += 1

        backFlag[i] = w
        for x in range(1, N + 1):
            if backCheckSum[i][x] == -1: continue
            heapq.heappush(backMap, (w + backCheckSum[i][x], x))

for x in range(1, N + 1):
    frontFlag[x] += backFlag[x]

print(max(frontFlag))
