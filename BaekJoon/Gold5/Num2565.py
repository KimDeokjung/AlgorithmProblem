import sys
input = sys.stdin.readline

def bin_search(checkSum, num):
    left = -1
    right = len(checkSum)

    while left + 1 < right:
        mid = (left + right) // 2

        if num > checkSum[mid]:
            left = mid
        else:
            right = mid

    return right

N = int(input())
inputData = []
checkSum = [0]
flag = []
maxNum = -1
result = []

for x in range(N): inputData.append(list(map(int, input().split())))
inputData.sort()



for x in range(N):
    aData = inputData[x][0]
    data = inputData[x][1]

    if checkSum[-1] < data:
        checkSum.append(data)
        flag.append([len(checkSum) - 1, aData])
        maxNum = max(maxNum, len(checkSum) - 1)
    else:
        index = bin_search(checkSum, data)
        checkSum[index] = data
        flag.append([index, aData])
        maxNum = max(maxNum, index)

for x, y in flag[::-1]:
    if x == maxNum:
        maxNum -= 1
        continue
    else:
        result.append(y)

print(len(result))

