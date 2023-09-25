result = list()
while True:
    T = int(input())
    resultData = list()
    if T == 0: break

    inputData = list()
    for x in range(T):
        tmp = input().split()
        tmp2 = list()
        for index, y in enumerate(tmp[1:]):
            if y == "N":
                tmp2.append(index + 1)

        inputData.append([tmp[0], tmp2])

    for x in range(T):
        for y in inputData[x][1]:
            B = inputData[x][0]
            A = inputData[x - y][0]
            resultData.append(A + " was nasty about " + B)

    result.append(resultData)


for x in range(len(result)):
    print("Group " + str(x + 1))

    for y in result[x]:
        print(y)
    if len(result[x]) == 0:
        print("Nobody was nasty")

    print()