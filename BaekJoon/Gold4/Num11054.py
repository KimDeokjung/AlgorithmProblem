N = int(input())
checkSum = []
inputData = list(map(int, input().split()))
result = 0

upFlag = [-1]
for x in range(N):
    downFlag = [10001]

    if upFlag[-1] < inputData[x]:
        upFlag.append(inputData[x])
    else:
        for z in range(len(upFlag) - 1, 0, -1):
            if upFlag[z] > inputData[x] > upFlag[z - 1]:
                upFlag[z] = inputData[x]
                break

    for y in inputData[x:]:
        if downFlag[-1] > y:
            downFlag.append(y)
        else:
            for z in range(len(downFlag) - 1, 0, -1):
                if downFlag[z] < y < downFlag[z - 1]:
                    downFlag[z] = y
                    break
    result = max(len(upFlag) + len(downFlag) - 3, result)

print(result)