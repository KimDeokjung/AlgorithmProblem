inputData = [[0 for _ in range(100)] for __ in range(100)]

for _ in range(4):
    x, y, i, j = map(int, input().split())

    for k in range(x, i):
        for z in range(y, j):
            inputData[k][z] = 1


result = 0
for x in inputData:
    result += sum(x)

print(result)