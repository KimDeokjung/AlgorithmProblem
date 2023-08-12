import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
result = []

def abc(inputData, checkSum, flag, a):
    if a not in flag:
        return inputData[a - 1]

    tmp = 0
    for x in flag[a]:
        if x in checkSum:
            tmp = max(tmp, checkSum[x])
        else:
            nowCost = abc(inputData, checkSum, flag, x)
            tmp = max(tmp, nowCost)
            checkSum[x] = nowCost
    return tmp + inputData[a - 1]

for _ in range(int(input())):
    N, K = map(int, input().split())
    inputData = list(map(int, input().split()))
    checkSum = dict()
    flag = dict()

    for __ in range(K):
        a, b = map(int, input().split())
        if b in flag:
            flag[b].add(a)
        else:
            flag[b] = {a}

    result.append(abc(inputData, checkSum, flag, int(input())))

print(*result)