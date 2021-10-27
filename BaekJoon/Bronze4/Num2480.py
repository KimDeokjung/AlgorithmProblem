# https://www.acmicpc.net/problem/2480

a=list(map(int,input().split()))
b=1000
if a.count(a[0])==3:print(10*b+a[0]*b)
elif a.count(a[0])==2:print(b+a[0]*100)
elif a.count(a[1])==2:print(b+a[1]*100)
else:print(max(a)*100)