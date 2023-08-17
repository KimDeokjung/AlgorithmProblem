import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
checkSum = [[] for _ in range(G + 1)]
result = 0

for x in range(P):
    if len(checkSum[0]) > 0:
        break

    result += 1
    g = int(input())

    if len(checkSum[g]) == 0:
        checkSum[g].append(g - 1)
    elif len(checkSum[checkSum[g][0]]) == 0:
        checkSum[checkSum[g][0]] = checkSum[g]
        checkSum[g][0] -= 1
    else:
        tmp = g
        while True:
            tmp = checkSum[tmp][0]
            if len(checkSum[tmp]) == 0:
                checkSum[tmp] = checkSum[g]
                checkSum[g][0] = tmp - 1
                break

if len(checkSum[0]) > 0: result -= 1
print(result)

