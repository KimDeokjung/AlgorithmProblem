T = int(input())
totalResult = []

for _ in range(T):
    n = int(input())
    inputData = list(map(int,input().split()))
    flag = set()
    result = 0

    for x in range(n):
        inputData[x] = inputData[x] - 1

    for index, x in enumerate(inputData):
        if index in flag: continue
        elif x in flag:
            flag.add(index)
            continue
        elif x == index:
            flag.add(index)
            result += 1
            continue

        tmp = [index]
        newFlag = set()
        newFlag.add(index)
        checkSum = x
        while True:
            tmp.append(checkSum)
            newFlag.add(checkSum)

            if inputData[checkSum] == checkSum or inputData[checkSum] in newFlag or inputData[checkSum] in flag:
                break

            checkSum = inputData[checkSum]

        if checkSum == inputData[checkSum]:
            result += 1
        elif inputData[checkSum] in newFlag:
            tmp2 = tmp.index(inputData[checkSum])
            result += (len(tmp) - tmp2)

        for z in tmp:
            flag.add(z)

    totalResult.append(n - result)

print(*totalResult)
