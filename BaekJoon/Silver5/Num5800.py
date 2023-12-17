inputData = list()
for _ in range(int(input())):inputData.append(sorted(list(map(int, input().split()))[1:]))

for x in range(len(inputData)):
	print("Class " + str(x + 1))
	tmp = 0
	maxData = max(inputData[x])
	minData = min(inputData[x])
	for y in range(len(inputData[x]) - 1):
		tmp = max(tmp, inputData[x][y + 1] - inputData[x][y])
	print(f"Max {maxData}, Min {minData}, Largest gap {tmp}")

