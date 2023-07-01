from itertools import combinations
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
checkSum = dict()
flag = set()
result = [0]

for x in range(1, N + 1):
    nowInput = list()

    tmp = list(map(int, input().split()))
    for y in range(1, len(tmp), 2):
        if tmp[y] != -1:
            nowInput.append((tmp[y], tmp[y + 1]))

    checkSum[tmp[0]] = nowInput

def abc(data):
    thisFlag = []
    maxLine = 0
    secondLine = 0

    if data in flag: return 0

    flag.add(data)

    for x in checkSum[data]:
        if x[0] not in flag:
            tmp = abc(x[0]) + x[1]
            if maxLine <= tmp:
                secondLine = maxLine
                maxLine = tmp
            elif secondLine < tmp:
                secondLine = tmp
            result[0] = max(result[0], maxLine)
            thisFlag.append([x[0], tmp])

    if len(thisFlag) == 0:
        return 0

    result[0] = max(result[0], maxLine + secondLine)

    return maxLine


abc(1)
print(*result)