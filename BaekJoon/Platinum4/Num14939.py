def switch(inputData, i, j):
    tmp = [(i, j), (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    for x, y in tmp:
        if 0 <= x < 10 and 0 <= y < 10:
            inputData[x][y] += 1
            inputData[x][y] %= 2

inputData = []
checkSum = [[0 for _ in range(10)] for __ in range(10)]
result = -1
for x in range(10):
    tmp = list()
    for y in input():
        if y == "#": tmp.append(0)
        else: tmp.append(1)
    inputData.append(tmp)

for x in range(1024):
    for i in range(10):
        for j in range(10):checkSum[i][j] = inputData[i][j]

    nowResult = 0
    trash = x
    for y in range(10):
        if trash % 2 == 1:
            switch(checkSum, 0, y)
            nowResult += 1
        trash //= 2

    for i in range(9):
        for j in range(10):
            if checkSum[i][j] == 1:
                switch(checkSum, i + 1, j)
                nowResult += 1

    if sum(checkSum[9]) == 0:
        if result == -1: result = nowResult
        else: result = min(result, nowResult)


print(result)
