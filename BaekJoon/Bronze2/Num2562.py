#https://www.acmicpc.net/problem/2562

N=list()
for x in range(9):N.append(int(input()))
print(max(N),N.index(max(N))+1)