import copy

first = input()
second = input()
checkSum = dict()
flag = [-1]

for index, x in enumerate(first):
    if x in checkSum:
        checkSum[x].append(index)
    else:
        checkSum[x] = [index]

for x in range(len(second)):
    tmp = []
    nowCheckSum = copy.deepcopy(checkSum)
    for y in range(x, len(second)):
        if second[y] not in nowCheckSum and len(nowCheckSum[second[y]]) == 0: continue

