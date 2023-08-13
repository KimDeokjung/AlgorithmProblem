import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def abc(inputData, checkSum, level, x, y):
    if inputData[level] == 0: return 0
    nextLevel = level + 1

    target = inputData[level]
    if target == x or target == y:
        tmp = 0
        if (nextLevel * 100 + x * 10 + y) in checkSum:
            tmp = checkSum[nextLevel * 100 + x * 10 + y]
        else:
            tmp = abc(inputData, checkSum, nextLevel, x, y)
            checkSum[nextLevel * 100 + x * 10 + y] = tmp
        return tmp + 1

    tmp = 800000
    tmp2 = 0
    if (nextLevel * 100 + target * 10 + y) in checkSum:
        tmp2 = checkSum[nextLevel * 100 + target * 10 + y]
    else:
        tmp2 = abc(inputData, checkSum, nextLevel, target, y)
        checkSum[nextLevel * 100 + target * 10 + y] = tmp2
    if x == 0: tmp2 += 2
    elif abs(x - target) == 2: tmp2 += 4
    else: tmp2 += 3
    tmp = min(tmp2, tmp)

    if (nextLevel * 100 + x * 10 + target) in checkSum:
        tmp2 = checkSum[nextLevel * 100 + x * 10 + target]
    else:
        tmp2 = abc(inputData, checkSum, nextLevel, x, target)
        checkSum[nextLevel * 100 + x * 10 + target] = tmp2
    if y == 0: tmp2 += 2
    elif abs(y - target) == 2: tmp2 += 4
    else: tmp2 += 3
    tmp = min(tmp2, tmp)

    return tmp

inputData = list(map(int, input().split()))
checkSum = dict()

print(abc(inputData, checkSum, 0, 0, 0))