#https://www.acmicpc.net/problem/1157

b=[0]*26
a=input().upper()
for x in range(len(a)):b[ord(a[x])-65]+=1
c=sorted(b)
if c[24]==c[25]:print("?")
else:print(chr(b.index(c[25])+65))