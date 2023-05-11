def insertMaxHeap(data):
    maxHeap.append(data)
    maxHeapLen = len(maxHeap) - 1

    while maxHeapLen != 1:
        if maxHeap[maxHeapLen // 2] < maxHeap[maxHeapLen]:
            maxHeap[maxHeapLen // 2], maxHeap[maxHeapLen] = maxHeap[maxHeapLen], maxHeap[maxHeapLen // 2]
        else:
            break

        maxHeapLen //= 2

def deleteMaxHeap(maxFlag):
    if len(maxHeap) < 2: return maxFlag
    elif len(maxHeap) < 3:
        while True:
            if len(maxHeap) < 2: return maxFlag
            popData = maxHeap.pop(-1)

            if popData in maxFlag:
                tmp = maxFlag.index(popData)
                maxFlag = maxFlag[:tmp] + maxFlag[tmp + 1:]
            else:
                minFlag.append(popData)
                break

        return maxFlag
    else:
        maxHeap[1], maxHeap[-1] = maxHeap[-1], maxHeap[1]

        while True:
            if len(maxHeap) < 2: return maxFlag
            popData = maxHeap.pop(-1)

            if popData in maxFlag:
                tmp = maxFlag.index(popData)
                maxFlag = maxFlag[:tmp] + maxFlag[tmp + 1:]
            else:
                minFlag.append(popData)
                break

        tmp = 1

        while True:
            if len(maxHeap) - 1 < tmp * 2:
                return maxFlag
            elif len(maxHeap) - 1 < tmp * 2 + 1:
                if maxHeap[tmp] < maxHeap[tmp * 2]:
                   maxHeap[tmp], maxHeap[tmp * 2] = maxHeap[tmp * 2], maxHeap[tmp]
                return maxFlag
            elif maxHeap[tmp * 2] > maxHeap[tmp * 2 + 1]:
                if maxHeap[tmp] < maxHeap[tmp * 2]:
                   maxHeap[tmp], maxHeap[tmp * 2] = maxHeap[tmp * 2], maxHeap[tmp]
                   tmp = tmp * 2
                else:
                    return maxFlag
            else:
                if maxHeap[tmp] < maxHeap[tmp * 2 + 1]:
                   maxHeap[tmp], maxHeap[tmp * 2 + 1] = maxHeap[tmp * 2 + 1], maxHeap[tmp]
                   tmp = tmp * 2 + 1
                else:
                    return maxFlag


def insertMinHeap(data):
    minHeap.append(data)
    minHeapLen = len(minHeap) - 1

    while minHeapLen != 1:
        if minHeap[minHeapLen // 2] > minHeap[minHeapLen]:
            minHeap[minHeapLen // 2], minHeap[minHeapLen] = minHeap[minHeapLen], minHeap[minHeapLen // 2]
        else:
            break

        minHeapLen //= 2

def deleteMinHeap(minFlag):
    if len(minHeap) < 2: return minFlag
    elif len(minHeap) < 3:
        while True:
            if len(minHeap) < 2: return minFlag
            popData = minHeap.pop(-1)

            if popData in minFlag:
                tmp = minFlag.index(popData)
                minFlag = minFlag[:tmp] + minFlag[tmp + 1:]
            else:
                maxFlag.append(popData)
                break

        return minFlag
    else:
        minHeap[1], minHeap[-1] = minHeap[-1], minHeap[1]
        while True:
            if len(minHeap) < 2: return minFlag
            popData = minHeap.pop(-1)

            if popData in minFlag:
                tmp = minFlag.index(popData)
                minFlag = minFlag[:tmp] + minFlag[tmp + 1:]
            else:
                maxFlag.append(popData)
                break
        tmp = 1

        while True:
            if len(minHeap) - 1 < tmp * 2:
                return minFlag
            elif len(minHeap) - 1 < tmp * 2 + 1:
                if minHeap[tmp] > minHeap[tmp * 2]:
                   minHeap[tmp], minHeap[tmp * 2] = minHeap[tmp * 2], minHeap[tmp]
                return minFlag
            elif minHeap[tmp * 2] < minHeap[tmp * 2 + 1]:
                if minHeap[tmp] > minHeap[tmp * 2]:
                   minHeap[tmp], minHeap[tmp * 2] = minHeap[tmp * 2], minHeap[tmp]
                   tmp = tmp * 2
                else:
                    return minFlag
            else:
                if minHeap[tmp] > minHeap[tmp * 2 + 1]:
                   minHeap[tmp], minHeap[tmp * 2 + 1] = minHeap[tmp * 2 + 1], minHeap[tmp]
                   tmp = tmp * 2 + 1
                else:
                    return minFlag

T = int(input())
result = []

for _ in range(T):

    maxHeap = list()
    minHeap = list()
    maxFlag = list()
    minFlag = list()
    maxHeap.append(-1)
    minHeap.append(-1)

    for x in range(int(input())):
        case, num = input().split()
        num = int(num)

        if case == "I":
            insertMinHeap(num)
            insertMaxHeap(num)
        else:
            if num < 0:
                minFlag = deleteMinHeap(minFlag)
            else:
                maxFlag = deleteMaxHeap(maxFlag)

    while True:
        if len(maxHeap) < 2: break
        tmp = maxHeap[1]
        if tmp in maxFlag:
            maxFlag = deleteMaxHeap(maxFlag)
        else:
            break

    while True:
        if len(minHeap) < 2: break
        tmp = minHeap[1]
        if tmp in minFlag:
            minFlag = deleteMinHeap(minFlag)
        else:
            break

    if len(maxHeap) < 2:
        result.append("EMPTY")
    else:
        result.append([maxHeap[1], minHeap[1]])


for x in result:
    if x == "EMPTY": print("EMPTY")
    else: print(*x)
