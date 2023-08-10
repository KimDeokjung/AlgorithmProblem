import sys
input = sys.stdin.readline

def findRoot(checkSum, data):
    if data == checkSum[data]:
        return data

    root = findRoot(checkSum, checkSum[data])
    checkSum[data] = root
    return root

def unionA(checkSum, data1, data2):
    root1 = findRoot(checkSum, data1)
    root2 = findRoot(checkSum, data2)

    if root1 < root2:
        checkSum[data2] = root1
    else:
        checkSum[data1] = root2

n, m = map(int, input().split())
checkSum = []
result = 0
flag = True

for x in range(n):
    checkSum.append(x)

for x in range(m):
    a, b = map(int, input().split())
    rootA = findRoot(checkSum, a)
    rootB = findRoot(checkSum, b)

    if rootA == rootB:
        result = x + 1
        flag = False
        break
    else:
        unionA(checkSum, rootA, rootB)

if flag:
    print(0)
else:
    print(result)

