def searchPosition(listData, data):
    if listData[0][0] < data:
        return -1
    if listData[-1][0] > data:
        return len(listData)

    for x in range(len(listData) - 1):
        if listData[x][0] > data > listData[x + 1][0]:
            return x

def searchPosition_v2(listData, data):
    if listData[0][0] < data:
        return -1
    if listData[-1][0] > data:
        return len(listData)

    l = 0
    r = len(listData)
    m = (l + r) // 2

    while m != l and m != r:
        if listData[m][0] >= data:
            l = m
            m = (l + r) // 2
        else:
            r = m
            m = (l + r) // 2

    return l


N = int(input())
inputData = list(map(int, input().split()))

checksum = list()
result = [0] * N

for x in range(N):
    target = inputData[x]

    if len(checksum) == 0:
        checksum.append([target, x])
        continue

    point = searchPosition_v2(checksum, target)

    if point == -1:
        checksum = [[target, x]]
    elif point == len(checksum):
        result[x] = checksum[-1][1] + 1
        checksum.append([target, x])
    else:
        result[x] = checksum[point][1] + 1
        checksum = checksum[:point + 1]
        checksum.append([target, x])

print(*result)

