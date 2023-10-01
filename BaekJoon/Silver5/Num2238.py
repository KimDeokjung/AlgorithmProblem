import sys
input = sys.stdin.readline
U, N = map(int, input().split())
checkSum = dict()

for x in range(N):
    name, num = input().split()
    num = int(num)
    if num > U: continue
    if num in checkSum:
        checkSum[num][1] += 1
    else:
        checkSum[num] = [name, 1]

result = (N, "", U)
for x in sorted(checkSum.keys()):
    if checkSum[x][1] < result[0]:
        result = (checkSum[x][1], checkSum[x][0], x)

print(result[1], result[2])