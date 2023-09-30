N = int(input())

result = 5000000000

tmp = int(N ** .5)
for x in range(max(tmp - 10, 2), tmp + 10):
    for y in range(max(tmp - 10, 2), tmp + 10):
        if x * y < N: continue
        result = min(x + y, result)
        break

if N <= 4:
    print(4)
else:
    result -= 2
    print(result * 2)