import heapq
import sys
input = sys.stdin.readline

def findRoot(flag, data):
    if flag[data] == data:
        return data

    tmp = findRoot(flag, flag[data])
    flag[data] = tmp
    return tmp

def unionRoot(flag, data1, data2):
    root1 = findRoot(flag, data1)
    root2 = findRoot(flag, data2)

    if root1 < root2:
        flag[root2] = root1
    else:
        flag[root1] = root2
    return

n = int(input())
inputData = list()
checkSum = list()
flag = []
result = 0
for x in range(n):
    flag.append(x)

for x in range(n):
    a, b = map(float, input().split())
    inputData.append((a, b))

for x in range(n):
    for y in range(x + 1, n):
        a1, b1 = inputData[x]
        a2, b2 = inputData[y]

        starLen = (abs(a1 - a2) ** 2 + abs(b1 - b2) ** 2) ** .5
        heapq.heappush(checkSum, (starLen, x, y))

while len(checkSum) != 0:
    value, a, b = heapq.heappop(checkSum)

    rootA = findRoot(flag, a)
    rootB = findRoot(flag, b)

    if rootA != rootB:
        unionRoot(flag, rootA, rootB)
        result += value

print(round(result, 2))