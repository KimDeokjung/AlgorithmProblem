N = int(input())
inputData = list()
myData = int(input())

for x in range(N - 1):
    inputData.append(int(input()))

if len(inputData) == 0:
    print(0)
else:
    result = 0
    while True:
        maxData = max(inputData)
        if myData > maxData:
            break

        result += 1
        myData += 1
        inputData[inputData.index(maxData)] -= 1

    print(result)

