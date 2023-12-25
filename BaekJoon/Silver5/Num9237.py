n=input()
a=sorted(list(map(int,input().split())))[::-1]
for x in range(len(a)):a[x]+=x+1
print(max(a) + 1)