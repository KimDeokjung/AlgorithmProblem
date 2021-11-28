import bisect


# https://www.acmicpc.net/problem/1654

num, target = map(int,input().split())
inputData = []
resultData = []
for x in range(num):inputData.append(int(input()))

startP = 0
endP = sum(inputData) + 1
checkP = endP // 2

while endP - startP > 1:
    checkData = 0
    for x in inputData:
        checkData += x // checkP
    if checkData < target:
        endP = checkP
    else:
        resultData.append(checkP)
        startP = checkP
    checkP = (startP + endP) // 2

print(max(resultData))