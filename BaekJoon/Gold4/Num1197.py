import sys
input = sys.stdin.readline

def findA(checkSum, data):
    if checkSum[data] == data:
        return data

    checkSum[data] = findA(checkSum, checkSum[data])

    return checkSum[data]


def unionA(checkSum, data1, data2):
    root1 = findA(checkSum, data1)
    root2 = findA(checkSum, data2)

    if root2 < root1:
        checkSum[root1] = root2
    else:
        checkSum[root2] = root1


V, E = map(int, input().split())
inputData = []
checkSum = []
for x in range(V + 1):
    checkSum.append(x)

for x in range(E):
    a, b, v = map(int, input().split())
    inputData.append((v, a, b))

inputData.sort(key=lambda x : x[0])

result = 0

for v, a, b in inputData:
    if findA(checkSum, a) == findA(checkSum, b):
        continue

    unionA(checkSum, a, b)
    result += v

print(result)
