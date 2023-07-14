import heapq
import sys
input = sys.stdin.readline

n = int(input())
result = []

inputData = [[-1 for _ in range(n + 1)] for __ in range(n + 1)]

for x in range(int(input())):
    i, j, w = map(int, input().split())

    if inputData[i][j] == -1: inputData[i][j] = w
    else: inputData[i][j] = min(w, inputData[i][j])

for x in range(1, n + 1):
    tmp = []
    flag = [-1 for _ in range(n + 1)]
    flag[x] = 0
    nowNum = 1

    for y in range(1, n + 1):
        if inputData[x][y] == -1: continue
        else: heapq.heappush(tmp, (inputData[x][y], y))

    while len(tmp) != 0 and nowNum != n:
        w, y = heapq.heappop(tmp)

        if flag[y] == -1 or flag[y] > w:
            if flag[y] == -1:
                nowNum += 1

            flag[y] = w

            for z in range(1, n + 1):
                if inputData[y][z] == -1: continue

                heapq.heappush(tmp, (w + inputData[y][z], z))

    for y in range(len(flag)):
        if flag[y] == -1:
            flag[y] = 0

    result.append(flag)

for x in result:
    print(*x[1:])