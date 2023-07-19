def abc(a, b):
    c = [[0, 0], [0, 0]]

    for x in range(2):
        for y in range(2):
            for z in range(2):
                c[x][y] += a[x][z] * b[z][y]
                c[x][y] %= 1000000007

    return c

N = int(input())
fiboNum = [[1, 1], [1, 0]]

checkSum = dict()
checkSum[1] = fiboNum

tmp = 1

while True:
    if tmp * 2 <= N:
        tmp *= 2
        fiboNum = abc(fiboNum, fiboNum)
        checkSum[tmp] = fiboNum
    else:
        break

N -= tmp

while N != 0:
    tmp = 1

    while True:
        if tmp * 2 <= N:
            tmp *= 2
        else:
            break

    N -= tmp
    fiboNum = abc(fiboNum, checkSum[tmp])

print(fiboNum[1][0])