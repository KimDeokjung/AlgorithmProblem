N, M = map(int, input().split())
inputData = [[0 for _ in range(M + 2)]]
result = 0
cheeseNum = 0

for x in range(N):
    tmp = [0]
    tmp += list(map(int, input().split()))
    cheeseNum += sum(tmp)
    tmp.append(0)
    inputData.append(tmp)

inputData.append([0 for _ in range(M + 2)])


while cheeseNum != 0:
    result += 1
    ways = [(0, 0)]
    visited = set()
    visited.add(0)
    checkSum = dict()
    deletePoint = set()

    while len(ways) != 0:
        xPoint, yPoint = ways.pop()
        flag = [(xPoint - 1, yPoint), (xPoint + 1, yPoint), (xPoint, yPoint - 1), (xPoint, yPoint + 1)]

        for x, y in flag:
            if -1 < x < N + 2 and -1 < y < M + 2 and (x * 1000 + y) not in visited:
                if inputData[x][y] == 0:
                    ways.append((x, y))
                    visited.add(x * 1000 + y)
                if inputData[x][y] == 1:
                    if (x * 1000 + y) not in checkSum:
                        checkSum[x * 1000 + y] = 1
                    else:
                        deletePoint.add(x * 1000 + y)

    for deleteCheese in deletePoint:
        x = deleteCheese // 1000
        y = deleteCheese % 1000
        inputData[x][y] = 0
        cheeseNum -= 1

print(result)