n, M = map(int, input().split())
result = 0
for x in range(1, n + 1):
	for y in str(x):
		if int(y) == M: result += 1

print(result)