from itertools import combinations

def findA(inputData, inputLen):
    result = dict()

    for x in range(1, inputLen + 1):
        for y in combinations(inputData, x):
            tmp = sum(y)
            if tmp in result: result[tmp] += 1
            else: result[tmp] = 1

    return result

N, S = map(int, input().split())
inputData = list(map(int, input().split()))
middle = N // 2
leftInputData = inputData[:middle]
rightInputData = inputData[middle:]
leftResult = findA(leftInputData, len(leftInputData))
rightResult = findA(rightInputData, len(rightInputData))
result = 0

for x in leftResult:
    if S - x in rightResult: result += rightResult[S - x] * leftResult[x]

if S in leftResult:
    result += leftResult[S]
if S in rightResult:
    result += rightResult[S]

print(result)