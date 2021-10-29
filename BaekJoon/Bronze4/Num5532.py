# https://www.acmicpc.net/problem/5532

a=[]
for x in range(5):a.append(int(input())-1)
print(a[0]-max(a[1]//(a[3]+1),a[2]//(a[4]+1)))
