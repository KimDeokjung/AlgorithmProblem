from itertools import combinations_with_replacement

N, M = map(int, input().split())
inputData = list(map(int, input().split()))
inputData.sort()

checkSum = set()

for i in combinations_with_replacement(inputData, M):
    tmp = str(i)

    if tmp in checkSum:
        continue
    else:
        checkSum.add(str(i))
        print(*i)