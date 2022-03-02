#https://www.acmicpc.net/problem/10816

storedData = {}
result = list()

N = int(input())
inputData = list(input().split())

for x in inputData:
    if x in storedData:
        storedData[x] += 1
    else:
        storedData[x] = 1

M = int(input())
resultData = list(input().split())

for x in resultData:
    if x in storedData:
        result.append(storedData[x])
    else:
        result.append("0")

print(*result)