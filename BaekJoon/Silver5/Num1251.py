from itertools import combinations

inputData = input()
lenData = len(inputData)

beforeData = (0, "")
result = "z" * lenData
for x in combinations(range(1, lenData), 2):
    if beforeData[0] == x[0]:
        tmp = beforeData[1]
    else:
        tmp = inputData[0:x[0]][::-1]
        beforeData = (x[0], tmp)

    nowResult = tmp + inputData[x[0]: x[1]][::-1] + inputData[x[1]:][::-1]
    result = min(result, nowResult)

print(result)
