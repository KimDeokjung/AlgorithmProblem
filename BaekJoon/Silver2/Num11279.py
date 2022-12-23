def insertHeap(inputList, newIndex):
    inputList.append(newIndex)
    nowIndex = len(inputList) - 1
    while nowIndex != 0:
        if inputList[nowIndex // 2] < inputList[nowIndex]:
            inputList[nowIndex // 2], inputList[nowIndex] = inputList[nowIndex], inputList[nowIndex // 2]
        nowIndex = nowIndex // 2

def popHeap(inputList):
    if len(inputList) == 0: return 0
    elif len(inputList) == 1: return inputList.pop()
    result = inputList[0]
    inputList[0] = inputList.pop()
    maxIndex = len(inputList) - 1
    targetIndex = 0

    while targetIndex * 2 + 1 <= maxIndex:
        if targetIndex * 2 + 2 > maxIndex:
            inputList[targetIndex * 2 + 1], inputList[targetIndex] = inputList[targetIndex], inputList[targetIndex * 2 + 1]
            targetIndex = targetIndex * 2 + 1
        else:
            target = targetIndex * 2 + 1 if inputList[targetIndex * 2 + 1] > inputList[targetIndex * 2 + 2] else targetIndex * 2 + 2
            if inputList[target] > inputList[targetIndex]:
                inputList[target], inputList[targetIndex] = inputList[targetIndex], inputList[target]
                targetIndex = target
            else:break
    return result


heap = []
result = []

for x in range(int(input())):
    num = int(input())
    if num == 0:
        result.append(popHeap(heap))
    else:
        insertHeap(heap, num)
    print(heap)
    print(result)
    print("-=-=-=-=")


print(*result)
