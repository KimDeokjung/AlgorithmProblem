checkSum = ["U", "C", "P", "C"]
flag = 0

for x in input():
	if flag == 4: break
	if x == checkSum[flag]:
		flag += 1

if flag == 4:
	print("I love UCPC")
else:
	print("I hate UCPC")