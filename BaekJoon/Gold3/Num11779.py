import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

inputData = [[-1 for _ in range(n + 1)] for __ in range(n + 1)]
for x in range(m):
    i, j, w = map(int, input().split())

    if inputData[i][j] == -1:
        inputData[i][j] = w
    else:
        inputData[i][j] = min(w, inputData[i][j])

startP, endP = map(int, input().split())

checkSum = []

for x in range(n + 1):
    if inputData[startP][x] == -1: continue

    heapq.heappush(checkSum, (inputData[startP][x], x, [startP, x]))

flag = [-1 for _ in range(n + 1)]
flagNum = 1
flag[startP] = 0

result = -1
resultLog = []

while True:
    if len(checkSum) == 0 or flagNum == n: break

    w, point, logs = heapq.heappop(checkSum)
    if point == endP:
        if result == -1 or result > w:
            result = w
            resultLog = logs

    if flag[point] == -1 or flag[point] > w:
        if flag[point] == -1: flagNum += 1
        flag[point] = w

        for x in range(n + 1):
            if inputData[point][x] == -1: continue
            heapq.heappush(checkSum, (w + inputData[point][x], x, logs + [x]))

print(result)
print(len(resultLog))
print(*resultLog)