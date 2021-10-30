# https://www.acmicpc.net/problem/6764

a=[]
for x in range(4):a.append(input())
b=len(set().union(a))
if b==1:print("Fish At Constant Depth")
elif b<4:print("No Fish")
elif a==sorted(a):print("Fish Rising")
else:print("Fish Diving")


