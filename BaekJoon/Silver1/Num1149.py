N = int(input())
inputData = []
flag = dict()

for x in range(N): flag[x] = [0, 0, 0]

r, g, b = map(int, input().split())
flag[0] = [r, g, b]

for x in range(1, N):
    r, g, b = map(int, input().split())

    flag[x][0] = min(flag[x - 1][1] + r, flag[x - 1][2] + r)
    flag[x][1] = min(flag[x - 1][0] + g, flag[x - 1][2] + g)
    flag[x][2] = min(flag[x - 1][0] + b, flag[x - 1][1] + b)

print(min(flag[N - 1]))
