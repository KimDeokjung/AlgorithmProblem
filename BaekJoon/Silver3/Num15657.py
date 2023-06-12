N, M = map(int, input().split())

inputData = list(map(int, input().split()))
inputData.sort()
checkSum = [0 for x in range(M)]


def abc(depth, data, flag):
    if flag + 1 > N: return

    if depth == M - 1:
        for x in range(flag, N):
            data[depth] = inputData[x]
            print(*data)
        return

    for x in range(flag, N):
        data[depth] = inputData[x]
        abc(depth + 1, data, x)


if M == 1:
    print(*inputData)
else:
    for x in range(N):
        checkSum[0] = inputData[x]
        abc(1, checkSum, x)
