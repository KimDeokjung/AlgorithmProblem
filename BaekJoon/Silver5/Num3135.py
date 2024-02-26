A, B = map(int, input().split())
checkSum = list()

for _ in range(int(input())): checkSum.append(int(input()))

result = abs(A - B)
for x in checkSum:
    result = min(result, abs(x - B) + 1)

print(result)