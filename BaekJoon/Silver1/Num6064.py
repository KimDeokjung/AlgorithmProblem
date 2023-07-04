T = int(input())
totalResult = []

for _ in range(T):
    M, N, x, y = map(int, input().split())
    x -= 1
    y -= 1

    tmp = startY = x % N
    result = 0
    flag = M - N

    if y == startY:
        result += x
        result += 1
    else:
        startY += flag
        startY %= N
        result += M

        while True:
            if startY == tmp:
                result = -1
                break
            elif y == startY:
                result += x
                result += 1
                break
            startY += flag
            startY %= N
            result += M

    totalResult.append(result)

print(*totalResult)
