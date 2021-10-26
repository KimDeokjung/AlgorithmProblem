## https://www.acmicpc.net/problem/10430

a,b,c=map(int,input().split())
d,e=(a+b)%c,a*b%c
print(d,d,e,e)