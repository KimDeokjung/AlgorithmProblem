import heapq

import sys
input = sys.stdin.readline

V, E = map(int, input().split())
startP = int(input())
inputData = dict()
for x in range(1, V + 1): inputData[x] = dict()
flag = [-1 for _ in range(V + 1)]
checkSum = []

for x in range(E):
    u, v, w = map(int, input().split())

    if v not in inputData[u]: inputData[u][v] = w
    else: inputData[u][v] = min(w, inputData[u][v])

    if u == startP: heapq.heappush(checkSum, (w, v))


tmp = 1
flag[startP] = 0
while tmp != V:
    if len(checkSum) == 0: break

    w, v = heapq.heappop(checkSum)

    if flag[v] == -1:
        tmp += 1
        flag[v] = w
        for x in inputData[v]:
            heapq.heappush(checkSum, (inputData[v][x] + w, x))
    elif flag[v] > w:
        flag[v] = w
        for x in inputData[v]:
            heapq.heappush(checkSum, (inputData[v][x] + w, x))
    else: continue


for x in flag[1:]:
    if x == -1: print("INF")
    else: print(x)