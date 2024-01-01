P = int(input())
result = []

for x in range(P):
	checkSum = list(map(int, input().split()))
	nowResult = 0
	for i in range(1, len(checkSum) - 1):
		for j in range(i + 1, len(checkSum)):
			if checkSum[i] > checkSum[j]:
				checkSum[i], checkSum[j] = checkSum[j], checkSum[i]
				nowResult += 1
	result.append(nowResult)

for x in range(P):
	print(f"{x + 1} {result[x]}")