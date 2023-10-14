target = input()
N = int(input())
result = 0
for x in range(N):
    tmp = input()
    tmp += tmp
    if target in tmp: result += 1

print(result)