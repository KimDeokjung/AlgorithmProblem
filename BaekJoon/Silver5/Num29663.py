def abc(checkSum, i, j, x, y):
    tmp = 0
    tmp += checkSum[x + 1][y + 1]
    tmp += checkSum[i][j]
    tmp -= checkSum[i][y + 1]
    tmp -= checkSum[x + 1][j]
    return tmp

n, m, s = map(int, input().split())
result = 0
inputData = list()
for x in range(n): inputData.append(list(map(int, input().split())))

checkSum = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
for x in range(1, n + 1):
    tmp = 0
    for y in range(1, m + 1):
        tmp += inputData[x - 1][y - 1]
        checkSum[x][y] = tmp + checkSum[x - 1][y]

for x in range(min(n, m)):
    for i in range(n - x):
        for j in range(m - x):
            if abc(checkSum, i, j, i + x, j + x) < s: result += 1

print(result)