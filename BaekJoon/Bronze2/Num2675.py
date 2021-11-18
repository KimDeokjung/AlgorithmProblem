#https://www.acmicpc.net/problem/2675

R=[]
for x in range(int(input())):
    T=""
    N,S=input().split()
    for y in S:T+=y*int(N)
    R.append(T)
print(*R)

