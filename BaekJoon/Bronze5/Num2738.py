N, M = map(int, input().split())
A = []
B = []

for x in range(N):
    A.append(list(map(int, input().split())))

for x in range(N):
    B.append(list(map(int, input().split())))

for x in range(N):
    for y in range(M):
        A[x][y] += B[x][y]

for x in A:
    print(*x)