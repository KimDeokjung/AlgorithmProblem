from itertools import combinations

N = int(input())
a = [1, 1]
b = 2
c = 1
while True:
    tmp = c * b
    a.append(tmp)
    if tmp > N: break
    c = tmp
    b += 1
lenData = len(a)

for x in range(1, lenData + 1):
    for y in combinations(a, x):
        if sum(y) == N:
            print("YES")
            exit()

print("NO")
