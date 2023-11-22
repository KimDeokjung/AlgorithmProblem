checkSum = [0 for _ in range(10001)]
checkSum[0] = 1

for x in range(1, 10000):
    tmp = x
    result = x
    while tmp != 0:
        result += (tmp % 10)
        tmp //= 10
    if result < 10000:
        checkSum[result] = 1

for x in range(1, 10000):
    if checkSum[x] == 0: print(x)