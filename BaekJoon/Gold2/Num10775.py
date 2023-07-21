import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
checkSum = dict()

tmp = int(input())
checkSum[tmp] = tmp
maxData = tmp
minData = tmp

for x in range(P - 1):
    data = int(input())

    if data in checkSum:
        checkSum[data] -= 1

        if checkSum[data] in checkSum:
            checkSum[data] = checkSum[checkSum[data]]
            checkSum.pop(checkSum[data])

        if checkSum[data] == 0:
            break
    elif data == maxData + 1:
        checkSum[data] = checkSum[maxData]
        checkSum.pop(maxData)
    elif data > maxData + 1:
        checkSum[data] = checkSum
    else:
        pass
