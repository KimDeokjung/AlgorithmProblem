a=[1,1]
for x in range(int(input())-1):a[x%2]=sum(a)
print(2*sum(a))