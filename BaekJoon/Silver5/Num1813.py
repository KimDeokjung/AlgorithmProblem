import collections

answer = -1
N = int(input())
inputData = list(map(int, input().split()))
checkSum = collections.Counter(inputData)
if 0 not in checkSum:
    checkSum[0] = 0

for x in range(51):
    if x in checkSum:
        if x == checkSum[x]: answer = x

print(answer)