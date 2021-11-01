# https://www.acmicpc.net/problem/8723

a=sorted(list(map(int,input().split())))
if(len(set(a).union())==1):print(2)
elif(a[0]**2+a[1]**2==a[2]**2):print(1)
else:print(0)