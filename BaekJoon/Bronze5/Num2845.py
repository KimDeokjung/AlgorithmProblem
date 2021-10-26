# https://www.acmicpc.net/problem/2845

a,b=map(int,input().split(" "))
c=list(map(int,input().split(" ")))
for x in c:print(x-b*a,end=" ")