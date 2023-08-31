import sys
input = sys.stdin.readline

def findRoot(flag, data):
    if flag[data] == data:
        return data

    rootD = findRoot(flag, flag[data])
    flag[data] = rootD
    return rootD

def unionRoot(flag, dataA, dataB):
    rootA = findRoot(flag, dataA)
    rootB = findRoot(flag, dataB)

    if rootA < rootB:
        flag[rootB] = rootA
    else:
        flag[rootA] = rootB

inputList = [[], [], []]
resultNum = 0
result = 0

N = int(input())
flag = []
checkSum = []

for _ in range(N):
    x, y, z = map(int, input().split())
    inputList[0].append((x, y, z, _))
    inputList[1].append((x, y, z, _))
    inputList[2].append((x, y, z, _))
    flag.append(_)

inputList[0].sort(key=lambda x:x[0])
inputList[1].sort(key=lambda x:x[1])
inputList[2].sort(key=lambda x:x[2])

for x in range(N - 1):
    for y in range(3):
        value = inputList[y][x + 1][y] - inputList[y][x][y]
        checkSum.append((value, inputList[y][x + 1][3], inputList[y][x][3]))

checkSum.sort(key=lambda x:x[0])

for x in range(len(checkSum)):
    v, a, b = checkSum[x]

    rootA = findRoot(flag, a)
    rootB = findRoot(flag, b)
    if rootA == rootB: continue
    else:
        unionRoot(flag, rootA, rootB)
        result += v
        resultNum += 1

    if resultNum == N - 1: break


print(result)
