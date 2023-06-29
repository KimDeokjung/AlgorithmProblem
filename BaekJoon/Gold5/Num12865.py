N, K = map(int, input().split())

checkSum = [[0 for _ in range(K + 1)] for __ in range(N + 1)]

for x in range(N):
    w, v = map(int, input().split())

    for y in range(K + 1):
        checkSum[x][y] = checkSum[x - 1][y]

    for y in range(K + 1):
        if y + w <= K:
            checkSum[x][y + w] = max(checkSum[x - 1][y] + v, checkSum[x - 1][y + w])

print(max(checkSum[-2]))
