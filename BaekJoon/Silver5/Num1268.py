N = int(input())

result = (-1, -1)
checkSum = [[set() for _ in range(9)] for __ in range(5)]
inputData = list()

for x in range(N):
    tmp = list(map(int, input().split()))
    inputData.append(tmp)
    for index, y in enumerate(tmp):
        checkSum[index][y - 1].add(x)

for point, datas in enumerate(inputData):
    tmp = set()
    for index, data in enumerate(datas):
        tmp = tmp.union(checkSum[index][data-1])
    if len(tmp) > result[0]: result = (len(tmp), point)

print(result[1] + 1)