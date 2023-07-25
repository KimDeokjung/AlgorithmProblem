def abc(n):
    result = []

    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            result.append(i)
            if (i ** 2) != n:
                result.append(n // i)
    return result


N = int(input())
inputData = list(map(int, input().split()))
checkSum = dict()
flag = set(inputData)

for x in inputData:
    checkSum[x] = 0

for x in inputData:
    for y in abc(x):
        if y in flag:
            checkSum[y] += 1
            checkSum[x] -= 1

for x in inputData:
    print(checkSum[x], end=" ")

