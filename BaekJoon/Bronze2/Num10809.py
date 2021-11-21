#https://www.acmicpc.net/problem/10809

R=[-1]*26
a=input()
for x in range(len(a)):
    if R[ord(a[x])-97] == -1:R[ord(a[x])-97] = x
print(*R)