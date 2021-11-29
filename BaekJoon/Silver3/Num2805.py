# https://www.acDmicpc.net/problem/2805

import sys
input = sys.stdin.readline

num, target = map(int, input().split())
inputData = list(map(int,input().split()))

startP = 0
endP = max(inputData) + 1
targetP = endP // 2
result = list()

while targetP not in result:
    nowResult = 0
    for x in inputData:
        value = x - targetP
        if value > 0:nowResult += value
        if nowResult > target:break
    if nowResult < target:
        endP = targetP
    else:
        result.append(targetP)
        startP = targetP
    targetP = (endP + startP) // 2

print(max(result))