import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

diamonds = list()
bags = list()
checkSum = list()

diamondPoint = 0
bagPoint = 0
result = 0

for x in range(N):
    w, v = map(int, input().split())
    diamonds.append((w, v))

for x in range(K):
    bags.append(int(input()))

diamonds.sort(key=lambda x : x[0])
bags.sort()

while diamondPoint != N and bagPoint != K:
    if diamonds[diamondPoint][0] <= bags[bagPoint]:
        heapq.heappush(checkSum, (-diamonds[diamondPoint][1], diamonds[diamondPoint][0]))
        diamondPoint += 1
    else:
        if len(checkSum) == 0:
            bagPoint += 1
            continue
        newItem = heapq.heappop(checkSum)
        result += -newItem[0]
        bagPoint += 1

while len(checkSum) != 0 and bagPoint != K:
    newItem = heapq.heappop(checkSum)
    result += -newItem[0]
    bagPoint += 1

print(result)