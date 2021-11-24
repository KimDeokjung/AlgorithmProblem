# https://www.acmicpc.net/problem/2609

a,b = map(int,input().split())
lcm = a*b
dataA = list()
dataB = list()
check = 2
while a != 1:
    if a % check == 0: dataA.append(check); a /= check
    else: check += 1
check = 2
while b != 1:
    if b % check == 0: dataB.append(check); b /= check
    else: check += 1

gbc = 1
for x in dataA:
    if x in dataB:
        dataB.pop(dataB.index(x))
        gbc *= x
print(gbc, lcm // gbc)