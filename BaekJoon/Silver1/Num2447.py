
N = int(input())
result = [[1] * N for row in range(N)]
inputData = list()
point = 1
while point < N:
    inputData.append(point)
    point *= 3

for x in inputData:
    for y in range(x, N, x * 3):
        for z in range(x, N, x * 3):
            for i in range(x):
                for j in range(x):
                    result[y + i][z + j] = 0

for x in result:
    for y in x:
        print([" ", "*"][y], end="")
    print()
