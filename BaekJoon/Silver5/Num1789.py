S = int(input())
n = 1
tmp = 0

for x in range(100000):
    if tmp > S:
        print(x - 1)
        break
    tmp += n
    n += 1