inputData = []

lineNum = 200

for x in range(lineNum):
    inputData.append(input())

for x in range(lineNum // 2):
    for y in range(x + 1):
        print(inputData[x][2*y], end="")
        print(inputData[lineNum - 1 -x][2*y+1], end="")
    print()
