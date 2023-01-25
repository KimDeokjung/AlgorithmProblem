import sys
input = sys.stdin.readline

T = int(input())
result = list()

for x in range(T):
    nowNum, target = map(int, input().split())
    checkSum = dict()
    flag = list()

    checkSum[nowNum] = ""
    flag.append(nowNum)

    while nowNum != target:
        tmp = flag.pop(0)
        nowNum = tmp
        tmpNum = len(checkSum[tmp])
        D = (tmp * 2) % 10000
        S = (tmp - 1) % 10000
        L = (tmp % 1000) * 10 + tmp // 1000
        R = (tmp % 10) * 1000 + tmp // 10

        for y, yFlag in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            z = y in checkSum
            if (z and len(checkSum[y]) > (tmpNum + 1)) or not z:
                checkSum[y] = checkSum[tmp] + yFlag
                flag.append(y)

        if target in [D, S, L, R]:
            nowNum = target
            break

    result.append(checkSum[nowNum])

print(*result)
