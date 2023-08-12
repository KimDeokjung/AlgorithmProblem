T = int(input())
n = int(input())
nData = list(map(int, input().split()))
m = int(input())
mData = list(map(int, input().split()))
checkSum = dict()
result = 0

for x in range(m):
    tmp = mData[x]
    if tmp in checkSum:
        checkSum[tmp] += 1
    else:
        checkSum[tmp] = 1

    for y in range(x + 1, m):
        tmp += mData[y]
        if tmp in checkSum:
            checkSum[tmp] += 1
        else:
            checkSum[tmp] = 1

for x in range(n):
    tmp = nData[x]
    if (T - tmp) in checkSum:
        result += checkSum[T - tmp]

    for y in range(x + 1, n):
        tmp += nData[y]
        if (T - tmp) in checkSum:
            result += checkSum[T - tmp]

print(result)