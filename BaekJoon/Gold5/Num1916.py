import heapq

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

inputData = [[-1 for _ in range(N + 1)] for __ in range(N + 1)]

for _ in range(M):
    startP, endP, w = map(int, input().split())
    if startP == endP: continue

    if inputData[startP][endP] == -1:
        inputData[startP][endP] = w
    else:
        inputData[startP][endP] = min(w, inputData[startP][endP])

sP, eP = map(int, input().split())
flag = [-1 for _ in range(N + 1)]
checkSum = []
tmp = 1

for x in range(1, N + 1):
    if inputData[sP][x] == -1: continue
    heapq.heappush(checkSum, (inputData[sP][x], x))

flag[sP] = 0

while tmp != N:
    if len(checkSum) == 0: break
    w, v = heapq.heappop(checkSum)

    if flag[v] == -1:
        tmp += 1
        flag[v] = w
        for x in range(1, N + 1):
            if inputData[v][x] == -1: continue

            heapq.heappush(checkSum, (inputData[v][x] + w, x))
    elif flag[v] > w:
        flag[v] = w
        for x in range(1, N + 1):
            if inputData[v][x] == -1: continue

            heapq.heappush(checkSum, (inputData[v][x] + w, x))
    else: continue

print(flag[eP])