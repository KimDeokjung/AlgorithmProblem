N, M = map(int, input().split())

result = 0
tmp = M
if N == 0:
    print(0)
    exit()
for x in map(int, input().split()):
    if tmp + x > M:
        tmp = x
        result += 1
    else:
        tmp += x
print(result)