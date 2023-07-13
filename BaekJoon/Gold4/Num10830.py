def abc(a, b):
    tmp = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            flag = 0
            for x in range(N):
                flag += (a[i][x] * b[x][j])
                flag %= 1000
            tmp[i][j] = flag

    return tmp

N, B = map(int, input().split())

checkSum = dict()

inputData = []

for x in range(N):
    tmp = list(map(int, input().split()))
    for y in range(N):
        tmp[y] %= 1000
    inputData.append(tmp)
checkSum[1] = inputData

point = 1

while point * 2 <= B:
    inputData = abc(checkSum[point], checkSum[point])
    point *= 2
    checkSum[point] = inputData

B -= point
while B != 0:
    point = 1
    while point * 2 <= B:
        point *= 2

    inputData = abc(checkSum[point], inputData)
    B -= point

for x in inputData:
    print(*x)

