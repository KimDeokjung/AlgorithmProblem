# https://www.acDmicpc.net/problem/1966

num = int(input())
result = list()

for _ in range(num):
    dataNum, target = map(int, input().split())
    inputData = list(map(int,input().split()))
    targetValue = inputData[target]
    thisResult = 0
    inputData[target] = -1
    splitPoint = -1
    for y in range(10, targetValue, -1):
        for x in range(len(inputData)-1, -1, -1):
            if inputData[x] == y:
                if splitPoint == -1:splitPoint = x
                else: splitPoint -= 1
                inputData.pop(x)
                thisResult += 1
        if splitPoint != -1:
            inputData = inputData[splitPoint:] + inputData[:splitPoint]
        splitPoint = -1
    for x in range(len(inputData)):
        if inputData[x] == -1:result.append(thisResult + 1)
        elif inputData[x] == targetValue:thisResult += 1
print(*result)