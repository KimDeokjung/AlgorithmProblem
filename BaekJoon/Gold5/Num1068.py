def abc(checkSum, target):
    if len(checkSum[target]) == 0:
        return 1

    result = 0
    for x in checkSum[target]:
        result += abc(checkSum, x)
    return result

N = int(input())
inputData = list(map(int, input().split()))
target = int(input())
checkSum = dict()
root = -1

for x in range(N):
    checkSum[x] = set()

for x in range(N):
    if inputData[x] == -1:
        root = x
        continue
    checkSum[inputData[x]].add(x)

for x in range(N):
    if target in checkSum[x]:
        checkSum[x].remove(target)

if root == target:
    print(0)
else:
    print(abc(checkSum, root))