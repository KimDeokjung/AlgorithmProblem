import copy

N = int(input())

checksum = dict()
result = dict()

firstNum = 9

def findStairs(num, N, numString):
    numString += str(num)
    if N == 1:
        data = list()
        data.append({num})
        return data

    minNum = (N-1)*10 + (num - 1)
    plusNum = (N-1)*10 + (num + 1)

    if num == 9:
        if minNum in checksum:
            data = copy.deepcopy(checksum[minNum])
        else:
            data = findStairs(num - 1, N - 1,numString)
            checksum[minNum] = copy.deepcopy(data)
    elif num == 0:
        if plusNum in checksum:
            data = copy.deepcopy(checksum[plusNum])
        else:
            data = findStairs(num + 1, N - 1,numString)

            checksum[plusNum] = copy.deepcopy(data)
    else:
        if minNum in checksum:
            minData = copy.deepcopy(checksum[minNum])
        else:
            minData = findStairs(num - 1, N - 1,numString)
            checksum[minNum] = copy.deepcopy(minData)
        if plusNum in checksum:
            plusData = copy.deepcopy(checksum[plusNum])
        else:
            plusData = findStairs(num + 1, N - 1,numString)
            checksum[plusNum] = copy.deepcopy(plusData)
        data = minData + plusData

    for x in data:
        x.add(num)

    return data


def findStairs_v2(num, N, numString):
    numString += str(num)
    if N == 1:
        data = list()
        data.append({num})
        return data

    minNum = (N-1)*10 + (num - 1)
    plusNum = (N-1)*10 + (num + 1)

    if num == 9:
        if minNum in checksum:
            data = copy.deepcopy(checksum[minNum])
        else:
            data = findStairs(num - 1, N - 1,numString)
            checksum[minNum] = copy.deepcopy(data)
    elif num == 0:
        if plusNum in checksum:
            data = copy.deepcopy(checksum[plusNum])
        else:
            data = findStairs(num + 1, N - 1,numString)

            checksum[plusNum] = copy.deepcopy(data)
    else:
        if minNum in checksum:
            minData = copy.deepcopy(checksum[minNum])
        else:
            minData = findStairs(num - 1, N - 1,numString)
            checksum[minNum] = copy.deepcopy(minData)
        if plusNum in checksum:
            plusData = copy.deepcopy(checksum[plusNum])
        else:
            plusData = findStairs(num + 1, N - 1,numString)
            checksum[plusNum] = copy.deepcopy(plusData)
        data = minData + plusData

    for x in data:
        x.add(num)

    return data

print(findStairs(9, N,"").count({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}))