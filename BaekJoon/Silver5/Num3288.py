checkSum = ["U", "R", "D", "L"]
flag = {
	"U": 0,
	"R": 3,
	"D": 2,
	"L": 1,
}

inputData = []
N = int(input())
result = []

for x in range(N): inputData.append(list(input()))

for x in range(N - 1, -1, -1):
	for y in range(x, -1, -1):
		tmp = flag[inputData[x][y]]
		for z in range(tmp): result.append((N - x, y + 1))
		if x == 0:
			pass
		elif y == 0:
			inputData[x - 1][y] = checkSum[(flag[inputData[x - 1][y]] - tmp) % 4]
		else:
			inputData[x][y - 1] = checkSum[(flag[inputData[x][y - 1]] - tmp) % 4]
			if x != y:
				inputData[x - 1][y] = checkSum[(flag[inputData[x - 1][y]] - tmp) % 4]

for x in result:
	print(*x)