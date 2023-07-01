N = int(input())

flag = [[] for x in range(N + 1)]
result = [0 for y in range(N + 1)]
visited = set()
checkSum = []

for x in range(N - 1):
    a, b = map(int, input().split())

    flag[a].append(b)
    flag[b].append(a)

checkSum += flag[1]

visited.add(1)
for x in checkSum:
    visited.add(x)
    result[x] = 1

while len(checkSum) != 0:
    tmp = checkSum.pop(0)
    for x in flag[tmp]:
        if x not in visited:
            visited.add(x)
            result[x] = tmp
            checkSum.append(x)

print(*result[2:])