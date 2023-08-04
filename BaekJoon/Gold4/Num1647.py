import sys
input = sys.stdin.readline

def findRoot(checkSum, data):
    if checkSum[data] == data:
        return data
    checkSum[data] = findRoot(checkSum, checkSum[data])
    return checkSum[data]

def unionRoot(checkSum, data1, data2):
    rootA = findRoot(checkSum, data1)
    rootB = findRoot(checkSum, data2)

    if rootA < rootB:
        checkSum[rootB] = rootA
    else:
        checkSum[rootA] = rootB

N, M = map(int, input().split())
inputData = []
checkSum = [0 for _ in range(N + 1)]
homeCount = dict()
flag = 0
result = 0
maxData = 0

for x in range(1, N + 1):
    checkSum[x] = x

for _ in range(M):
    a, b, c = map(int, input().split())
    inputData.append([a, b, c])
inputData.sort(key=lambda x:x[2])

division = False
for a, b, c in inputData:
    rootA = findRoot(checkSum, a)
    rootB = findRoot(checkSum, b)

    if rootA == rootB: continue
    unionRoot(checkSum, rootA, rootB)
    result += c
    maxData = c

print(result - maxData)