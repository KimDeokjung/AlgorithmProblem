N = int(input())
checksum = dict()
result = list()
for x in input().split(): checksum[x] = 0

for _ in range(N):
    for x in input().split(): checksum[x] += 1

for x in checksum:
    result.append([x, checksum[x]])

result = sorted(result, key=lambda x:-x[1])
for x in result: print(*x)