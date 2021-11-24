# https://www.acmicpc.net/problem/1181

N=int(input())
data = []
for x in range(N):
    D = input()
    data.append((D,len(D)))
data = list(set(data))
result = sorted(data,key=lambda x:(x[1],x[0]))

for x in range(len(result)):print(result[x][0])