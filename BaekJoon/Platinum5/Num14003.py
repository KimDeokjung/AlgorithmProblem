def findIndex(checkSum, data):
    left = -1
    right = len(checkSum)

    while left + 1 < right:
        mid = (left + right) // 2

        if checkSum[mid] < data:
            left = mid
        else:
            right = mid

    return right


N = int(input())
inputData = list(map(int, input().split()))

checkSum = [-1000000001]
result = []
output = []
maxResult = 0

for x in inputData:
    if checkSum[-1] < x:
        checkSum.append(x)
        index = len(checkSum) - 1
        result.append((index, x))
        maxResult = max(maxResult, index)
    else:
        index = findIndex(checkSum, x)
        checkSum[index] = x
        result.append((index, x))
        maxResult = max(maxResult, index)


for x in result[::-1]:
    if maxResult == x[0]:
        output.append(x[1])
        maxResult -= 1

print(len(output))
print(*output[::-1])
