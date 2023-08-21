import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
checkSum = dict()
zeroData = list()
result = []
flag = [0 for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    flag[b] += 1
    if a in checkSum: checkSum[a].append(b)
    else: checkSum[a] = [b]

for x in range(1, N + 1):
    if flag[x] == 0:
        heapq.heappush(zeroData, x)

while len(zeroData) != 0:
    nowData = heapq.heappop(zeroData)
    if nowData in checkSum:
        for x in checkSum[nowData]:
            flag[x] -= 1
            if flag[x] == 0: heapq.heappush(zeroData, x)
    result.append(nowData)

print(" ".join(map(str, result)))