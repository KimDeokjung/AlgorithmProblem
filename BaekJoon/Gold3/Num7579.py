N, M = map(int, input().split())
application = [0] + list(map(int, input().split()))
coast = [0] + list(map(int, input().split()))
totalCoast = sum(coast)
checkSum = [[0 for _ in range(totalCoast + 1)] for __ in range(N + 1)]
result = 10001


for x in range(1, N + 1):
    for y in range(1, totalCoast + 1):
        if y < coast[x]: checkSum[x][y] = checkSum[x - 1][y]
        else:
            checkSum[x][y] = max(checkSum[x - 1][y - coast[x]] + application[x], checkSum[x - 1][y])
            if checkSum[x][y] >= M:
                result = min(result, y)

print(result)