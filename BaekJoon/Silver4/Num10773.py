# https://www.acmicpc.net/problem/10773

N = int(input())
result = list()

for x in range(N):
	inputData = input()
	if inputData == '0':
		result.pop()
	else:
		result.append(int(inputData))

print(sum(result))
