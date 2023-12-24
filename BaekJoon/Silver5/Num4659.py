result = []
checkSum = ("a", "e", "i", "o", "u")

while True:
	inputData = input()
	if inputData == "end": break
	flag = True
	isCheckSum = False

	for x in range(len(inputData)):
		if inputData[x] in checkSum: isCheckSum = True

		if x < len(inputData) - 2:
			if (inputData[x] in checkSum) == (inputData[x + 1] in checkSum) and (inputData[x + 1] in checkSum) == (inputData[x + 2] in checkSum):
				flag = False
		if x < len(inputData) - 1:
			if inputData[x] != "e" and inputData[x] != "o" and inputData[x] == inputData[x + 1]:
				flag = False

	result.append((inputData, flag and isCheckSum))

for x, y in result:
	if y:
		print(f"<{x}> is acceptable.")
	else:
		print(f"<{x}> is not acceptable.")