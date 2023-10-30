N = int(input())
inputData = set(map(int, input().split()))
M = int(input())
inputData2 = list(map(int, input().split()))
result = []

for x in inputData2:
    if x in inputData: result.append(1)
    else: result.append(0)

print(*result)