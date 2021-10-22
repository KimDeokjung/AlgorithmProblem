# https://www.acmicpc.net/problem/1085

a,b,c,d=map(int,input().split())
print(min(c-a,d-b,a,b))