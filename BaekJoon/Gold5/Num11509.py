N = int(input())
inputData = list(map(int, input().split()))
checkSum = dict()

totalResult = 0
for x in inputData:
    if x in checkSum and checkSum[x] != 0:
        checkSum[x] -= 1
        if x - 1 in checkSum:
            checkSum[x - 1] += 1
        else:
            checkSum[x - 1] = 1
    else:
        totalResult += 1
        if x - 1 in checkSum:
            checkSum[x - 1] += 1
        else:
            checkSum[x - 1] = 1

print(totalResult)