#https://www.acmicpc.net/problem/1620

from sys import stdin

N, M = map(int, input().split())
data = []
data_dic = {}
result = []

for x in range(N):
    d = stdin.readline()[:-1]
    data.append(d)
    data_dic[d] = x + 1

for x in range(M):
    flag = stdin.readline()[:-1]
    if flag.isdigit():
        result.append(data[int(flag) - 1])
    else:
        result.append(data_dic[flag])

print(" ".join(map(str,result)))