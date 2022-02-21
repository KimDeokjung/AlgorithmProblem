#https://www.acmicpc.net/problem/2839
N = int(input())

point = N // 5

for x in range(point, -1, -1):
    if (N - (5 * x)) % 3 == 0:
        print((N - (5 * x)) // 3 + x)
        break
else:
    print(-1)
