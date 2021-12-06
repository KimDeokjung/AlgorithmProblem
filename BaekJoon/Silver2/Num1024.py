#https://www.acmicpc.net/problem/1024

taget, con = map(int, input().split(" "))
sum = 0
posobel = False
result = list()
for x in range(con):
    sum += x

for x in range(con, con + (taget // con) + 1):
    if taget < sum:
        break
    if (taget - sum) % x == 0:
        for y in range(x):
            result.append((taget - sum) // x + y)
        posobel = True
        break
    else:
        sum += x
if not posobel or len(result) > 100:
    print(-1)
else:
    print(*result)