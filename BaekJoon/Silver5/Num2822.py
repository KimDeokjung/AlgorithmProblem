inputData = []
result = []
score = 0

for x in range(8):
    inputData.append((int(input()), x + 1))

inputData.sort(key = lambda x:-x[0])
for x in range(5):
    result.append(inputData[x][1])
    score += inputData[x][0]
result.sort()

print(score)
print(*result)