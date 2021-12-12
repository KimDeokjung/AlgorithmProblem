#https://www.acmicpc.net/problem/1929

M, N = map(int, input().split())
result = list()

if M < 3:
    M = 3
    if N > 1:
        result.append(2)

if M % 2 == 0:M += 1
for x in range(M, N + 1, 2):
    for y in range(3, int(x**.5) + 1, 2):
        if x % y == 0:break
    else:result.append(x)
print(*result)

