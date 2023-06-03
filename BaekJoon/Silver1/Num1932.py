inputData = [0]

N = int(input())
for x in range(N):
    inputData.append(list(map(int, input().split())))


checkSum = 1
flag = [0]
for x in range(1, N):
    tmp = [0 for _ in range(x + 1)]

    for y in range(x):
        tmp[y] = max([tmp[y], flag[y] + inputData[x][y]])
        tmp[y + 1] = max([tmp[y + 1], flag[y] + inputData[x][y]])

    flag = tmp

for x in range(N):
    flag[x] += inputData[N][x]

print(max(flag))
