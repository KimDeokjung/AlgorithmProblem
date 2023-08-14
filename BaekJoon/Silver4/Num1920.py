N = int(input())
checkSum = dict()
result = []

for x in list(map(int, input().split())):
    if x in checkSum: continue
    else: checkSum[x] = 1

M = int(input())
for x in list(map(int, input().split())):
    if x in checkSum: result.append(1)
    else: result.append(0)

print(*result)