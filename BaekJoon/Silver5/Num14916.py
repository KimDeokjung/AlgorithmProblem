N = int(input())

target = N // 2 + N % 2
numTwo = target
numFive = 0
result = 50001
target *= 2

while numTwo != -1:
    if target == N:
        result = min(numTwo + numFive, result)

    if target > N:
        numTwo -= 1
        target -= 2
    else:
        numFive += 1
        target += 5

if result == 50001:
    print(-1)
else:
    print(result)