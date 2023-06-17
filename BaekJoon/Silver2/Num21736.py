N, M = map(int, input().split())

inputData = list()
result = 0
startX = 0
startY = 0

for x in range(N):
    tmp = list(input())
    if "I" in tmp:
        startX = x
        startY = tmp.index("I")

    inputData.append(tmp)

checkSum = [(startX, startY)]
while len(checkSum) != 0:
    x, y = checkSum.pop(0)

    flag = list()
    if x - 1 >= 0 and inputData[x - 1][y] != "X":
        if inputData[x - 1][y] == "P": result += 1
        inputData[x - 1][y] = "X"
        checkSum.append((x - 1, y))
    if x + 1 < N and inputData[x + 1][y] != "X":
        if inputData[x + 1][y] == "P": result += 1
        inputData[x + 1][y] = "X"
        checkSum.append((x + 1, y))
    if y - 1 >= 0 and inputData[x][y - 1] != "X":
        if inputData[x][y - 1] == "P": result += 1
        inputData[x][y - 1] = "X"
        checkSum.append((x, y - 1))
    if y + 1 < M and inputData[x][y + 1] != "X":
        if inputData[x][y + 1] == "P": result += 1
        inputData[x][y + 1] = "X"
        checkSum.append((x, y + 1))


print(["TT", result][result != 0])