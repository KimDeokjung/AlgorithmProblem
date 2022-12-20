N = int(input())

data = []
result = []
for x in range(N): data.append(int(input()))

caseData = [1, 1, 1, 2, 2]
for x in range(4, max(data)):
    caseData.append(caseData[x] + caseData[x - 4])

for x in data:
    result.append(caseData[x - 1])

print(*result)
