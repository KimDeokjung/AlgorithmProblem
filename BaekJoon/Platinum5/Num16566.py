def findIndex(checkSum, data):
    left = -1
    right = len(checkSum)

    while left + 1 < right:
        mid = (left + right) // 2
        if checkSum[mid] <= data:
            left = mid
        else:
            right = mid

    return right

def findRoot(flag, data):
    if flag[data] == data:
        return data

    rootA = findRoot(flag, flag[data])
    flag[data] = rootA
    return rootA

def unionRoot(flag, dataA, dataB):
    rootA = findRoot(flag, dataA)
    rootB = findRoot(flag, dataB)

    if rootA > rootB:
        flag[rootB] = rootA
    else:
        flag[rootA] = rootB


N, M, K = map(int, input().split())
inputData = list(map(int, input().split()))
inputData.sort()
battle = list(map(int, input().split()))
flag = []
for x in range(M):
    flag.append(x)
result = []


for x in battle:
    index = findIndex(inputData, x)
    rootIndex = findRoot(flag, index)
    result.append(inputData[rootIndex])

    if rootIndex < M - 1:
        unionRoot(flag, rootIndex, rootIndex + 1)

print(*result)
