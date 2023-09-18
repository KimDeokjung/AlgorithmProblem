def abc(a, b):
    c = [[0 for _ in range(8)] for __ in range(8)]

    for x in range(8):
        for y in range(8):
            for z in range(8):
                c[x][y] += (a[x][z] * b[z][y])
                c[x][y] %= 1000000007

    return c

D = int(input())
inputData = []
point = 1
originData = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0]
]

result = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1]
]


while D != 0:
    tmp = 1

    while tmp < D:
        tmp *= 2

    if tmp != D: tmp //= 2
    inputData.append(tmp)
    D -= tmp

inputData.reverse()

while len(inputData) != 0:
    target = inputData.pop(0)

    while point != target:
        point *= 2
        originData = abc(originData, originData)

    result = abc(result, originData)

print(result[0][0])