inputData = input()
lenInputData = len(inputData)
checkSum = [[False for _ in range(lenInputData)] for __ in range(lenInputData)]
flag = [2500 for _ in range(lenInputData + 1)]
flag[-1] = 0

for x in range(lenInputData - 1):
    checkSum[x][x] = True
    if inputData[x] == inputData[x + 1]:
        checkSum[x][x + 1] = True
checkSum[lenInputData - 1][lenInputData - 1] = True

for x in range(3, lenInputData + 1):
    for y in range(lenInputData + 1 - x):
        z = y + x - 1
        if checkSum[y + 1][z - 1] and inputData[y] == inputData[z]:
            checkSum[y][z] = True

for end in range(lenInputData):
    for start in range(end + 1):
        if checkSum[start][end]:
            flag[end] = min(flag[end], flag[start - 1] + 1)
        else:
            flag[end] = min(flag[end], flag[end - 1] + 1)

print(flag[lenInputData - 1])