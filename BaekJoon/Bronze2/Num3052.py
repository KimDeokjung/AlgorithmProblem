#https://www.acmicpc.net/problem/3052

a=set()
for x in range(10):a.add(int(input())%42)
print(len(a))