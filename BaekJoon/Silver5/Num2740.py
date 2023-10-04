N, M = map(int, input().split())
A = list()
for x in range(N): A.append(list(map(int, input().split())))

I, K = map(int, input().split())
B = list()
for x in range(I): B.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for __ in range(N)]

for x in range(N):
    for y in range(K):
        tmp = 0
        for z in range(M):
            tmp += A[x][z] * B[z][y]
        result[x][y] = tmp

for x in result:
    print(*x)