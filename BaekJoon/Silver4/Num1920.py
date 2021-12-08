#https://www.acmicpc.net/problem/1920

N = int(input())
targetData = list(map(int,input().split()))
maxData = max(targetData)
minData = min(targetData)
M = int(input())
inputData = list(map(int,input().split()))
result = list()

for x in inputData:
    if x > maxData or x < minData: result.append(0)
    elif x in targetData:result.append(1)
    else:result.append(0)

print(*result)