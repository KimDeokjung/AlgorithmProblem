j = list(map(int, input().split()))
g = list(map(int, input().split()))

flag = False
totalJ = 0
totalG = 0
for x in range(9):
	totalJ += j[x]
	if totalJ > totalG:
		flag = True
	totalG += g[x]

if flag and totalG > totalJ: print("Yes")
else: print("No")