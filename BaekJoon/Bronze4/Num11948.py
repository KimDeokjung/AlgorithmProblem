# https://www.acmicpc.net/problem/11948

a = 0
b = []
c = []
for x in range(4):b.append(int(input()))
a -= min(b)
for y in range(2):c.append(int(input()))
a -= min(c)
print(sum(c) + sum(b) + a)