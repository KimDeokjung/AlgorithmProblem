T = int(input())
totalResult = []

for _ in range(T):
    n = int(input())
    inputData = [list(map(int, input().split())), list(map(int, input().split()))]
    checkSum = [[0 for _ in range(n)] for _ in range(2)]

    checkSum[0][0] = inputData[0][0]
    checkSum[1][0] = inputData[1][0]
    result = max(checkSum[0][0], checkSum[1][0])

    if n > 1:
        checkSum[0][1] = inputData[0][1] + inputData[1][0]
        checkSum[1][1] = inputData[1][1] + inputData[0][0]
        result = max(checkSum[0][1], checkSum[1][1])

    for x in range(2, n):
        checkSum[0][x] = inputData[0][x] + max(checkSum[0][x - 2], checkSum[1][x - 2], checkSum[1][x - 1])
        checkSum[1][x] = inputData[1][x] + max(checkSum[0][x - 2], checkSum[1][x - 2], checkSum[0][x - 1])

        result = max(checkSum[0][x], checkSum[1][x], result)

    totalResult.append(result)

print(*totalResult)