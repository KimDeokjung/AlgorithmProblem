# https://www.acmicpc.net/problem/5928

a,b,c=map(int,input().split())
d=60*(24*a+b-275)+c-11
print([d,-1][d<0])
