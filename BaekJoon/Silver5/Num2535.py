N = int(input())
inputData = []
result = []
checkSum = dict()

for x in range(N): inputData.append(list(map(int, input().split())))
inputData.sort(key=lambda x:-x[2])

for a, b, c in inputData:
    if a in checkSum and checkSum[a] == 1:
        checkSum[a] += 1
        result.append([a, b])
    elif a not in checkSum:
        checkSum[a] = 1
        result.append([a, b])
    if len(result) == 3: break

for x in result:
    print(*x)
