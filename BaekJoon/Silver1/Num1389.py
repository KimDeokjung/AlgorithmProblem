N, M = map(int, input().split())

flag = set()
inputSet = set()
checkSum = [[0]*N for _ in range(N)]
star = 0
targetNum = N*(N - 1)//2

for x in range(N):
    for y in range(x + 1, N):
        flag.add(1000 * x + y)

for x in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if checkSum[a][b] == 0:
        checkSum[a][b] = 1
        checkSum[b][a] = 1
        star += 1

while star != targetNum:

    for x in flag:
        a = x // 1000
        b = x % 1000
        lowNum = 99999

        for i in range(N):
            Aflag = checkSum[i][a]
            Bflag = checkSum[i][b]

            if Aflag != 0 and Bflag != 0:
                lowNum = min(lowNum, Aflag + Bflag)

        if lowNum != 99999:
            if checkSum[a][b] == 0:
                star += 1
                checkSum[a][b] = lowNum
                checkSum[b][a] = lowNum
            else:
                checkSum[a][b] = min(lowNum, checkSum[a][b])
                checkSum[b][a] = min(lowNum, checkSum[b][a])

for x in flag:
    a = x // 1000
    b = x % 1000
    lowNum = 99999

    for i in range(N):
        Aflag = checkSum[i][a]
        Bflag = checkSum[i][b]

        if Aflag != 0 and Bflag != 0:
            lowNum = min(lowNum, Aflag + Bflag)

    if lowNum != 99999:
        if checkSum[a][b] == 0:
            star += 1
            checkSum[a][b] = lowNum
            checkSum[b][a] = lowNum
        else:
            checkSum[a][b] = min(lowNum, checkSum[a][b])
            checkSum[b][a] = min(lowNum, checkSum[b][a])

resultData = 1
result = sum(checkSum[0])

for idx, x in enumerate(checkSum[1:]):
    k = sum(x)
    if k < result:
        result = k
        resultData = idx + 2

print(resultData)

