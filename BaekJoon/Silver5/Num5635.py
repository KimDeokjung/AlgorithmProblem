checkSum = list()

for _ in range(int(input())):
	a, b, c, d = input().split()
	b = int(b)
	c = int(c)
	d = int(d)
	checkSum.append((a, b, c, d))

checkSum.sort(key=lambda x:x[1])
checkSum.sort(key=lambda x:x[2])
checkSum.sort(key=lambda x:x[3])

print(checkSum[-1][0])
print(checkSum[0][0])
