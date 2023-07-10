import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
inputData = dict()
checkSum = dict()
flag = [True for _ in range(n + 1)]
result = [0]

for x in range(n - 1):
    parents, child, value = map(int, input().split())
    if parents not in inputData:
        inputData[parents] = [(child, value)]
    else:
        inputData[parents].append((child, value))

    if child not in inputData:
        inputData[child] = [(parents, value)]
    else:
        inputData[parents].append((parents, value))

def abc(value):
    if value not in inputData: return 0

    firstLen = 0
    secondLen = 0

    for x, value in inputData[value]:
        if not flag[x]: continue
        flag[x] = False
        tmp = 0
        if x in checkSum:
            tmp = checkSum[x]
        else:
            tmp = abc(x) + value
            checkSum[x] = tmp

        if tmp > firstLen:
            secondLen = firstLen
            firstLen = tmp
        elif tmp > secondLen:
            secondLen = tmp
        flag[x] = True

    result[0] = max(firstLen + secondLen, result[0])

    return firstLen

flag[1] = False
abc(1)
print(result[0])