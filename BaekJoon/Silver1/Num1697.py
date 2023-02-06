N, K = map(int, input().split())
flag = set()
flag.add(N)
resultData = [N, -1]

result = 0

while True:
    data = resultData.pop(0)
    if data == -1:
        result += 1
        resultData.append(-1)
        continue

    if data == K:break

    a, b, c = data - 1, data + 1, data * 2
    if K in [a, b, c]:
        result += 1
        break

    if a > -1 and a not in flag:
        flag.add(a)
        resultData.append(a)
    if b <= 100000 and b not in flag:
        flag.add(b)
        resultData.append(b)
    if c <= 100000 and c not in flag:
        flag.add(c)
        resultData.append(c)

print(result)
