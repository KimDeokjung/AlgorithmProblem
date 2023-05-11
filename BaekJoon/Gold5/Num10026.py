import copy

inputData = list()
N = int(input())
result = [0, 0]

for x in range(N):
    inputData.append(list(input()))

inputData_b = [[0 for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        if inputData[x][y] == "B": inputData_b[x][y] = "B"
        else: inputData_b[x][y] = "R"

for x in range(N):
    for y in range(N):
        if inputData[x][y] == "-": continue

        checkSum = inputData[x][y]
        flag = set()
        flag.add(x * 1000 + y)

        while True:
            if len(flag) == 0: break
            popData = flag.pop()
            xPoint = popData // 1000
            yPoint = popData % 1000

            inputData[xPoint][yPoint] = "-"

            if xPoint - 1 >= 0 and inputData[xPoint - 1][yPoint] == checkSum and (xPoint * 1000 + yPoint - 1000) not in flag: flag.add(xPoint * 1000 + yPoint - 1000)
            if yPoint - 1 >= 0 and inputData[xPoint][yPoint - 1] == checkSum and (xPoint * 1000 + yPoint - 1) not in flag: flag.add(xPoint * 1000 + yPoint - 1)
            if xPoint + 1 < N and inputData[xPoint + 1][yPoint] == checkSum and (xPoint * 1000 + yPoint + 1000) not in flag: flag.add(xPoint * 1000 + yPoint + 1000)
            if yPoint + 1 < N and inputData[xPoint][yPoint + 1] == checkSum and (xPoint * 1000 + yPoint + 1) not in flag: flag.add(xPoint * 1000 + yPoint + 1)

        result[0] += 1

for x in range(N):
    for y in range(N):
        if inputData_b[x][y] == "-": continue

        checkSum = inputData_b[x][y]
        flag = set()
        flag.add(x * 1000 + y)

        while True:
            if len(flag) == 0: break
            popData = flag.pop()
            xPoint = popData // 1000
            yPoint = popData % 1000

            inputData_b[xPoint][yPoint] = "-"

            if xPoint - 1 >= 0 and inputData_b[xPoint - 1][yPoint] == checkSum and (xPoint * 1000 + yPoint - 1000) not in flag: flag.add(xPoint * 1000 + yPoint - 1000)
            if yPoint - 1 >= 0 and inputData_b[xPoint][yPoint - 1] == checkSum and (xPoint * 1000 + yPoint - 1) not in flag: flag.add(xPoint * 1000 + yPoint - 1)
            if xPoint + 1 < N and inputData_b[xPoint + 1][yPoint] == checkSum and (xPoint * 1000 + yPoint + 1000) not in flag: flag.add(xPoint * 1000 + yPoint + 1000)
            if yPoint + 1 < N and inputData_b[xPoint][yPoint + 1] == checkSum and (xPoint * 1000 + yPoint + 1) not in flag: flag.add(xPoint * 1000 + yPoint + 1)

        result[1] += 1


print(*result)

