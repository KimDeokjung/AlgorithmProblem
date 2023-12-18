A, B = map(int, input().split())
m = int(input())
inputData = list(map(int, input().split()))
result = 0
nowResult = []
tmp = 1
for x in inputData[::-1]:
	result += tmp * x
	tmp *= A

while result != 0:
	nowResult.append(result % B)
	result //= B

print(*nowResult[::-1])