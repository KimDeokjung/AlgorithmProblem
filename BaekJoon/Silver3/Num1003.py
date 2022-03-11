N = int(input())
inputData = list()
result = list()
for x in range(N):inputData.append(int(input()))

for x in inputData:
    pibo = [[1, 0], [0, 1]]
    point = 0
    for y in range(x):
        pibo[point][0] = pibo[0][0] + pibo[1][0]
        pibo[point][1] = pibo[0][1] + pibo[1][1]
        point += 1
        point %= 2
    result.append(pibo[point])

for x in result:
    print(*x)
