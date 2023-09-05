import sys
input = sys.stdin.readline

N = int(input())
inputData = []
for x in range(N):
    a, b = map(int, input().split())
    inputData.append((a, x))
    inputData.append((b, x))
inputData.sort()
d = int(input())


nowLen = 0
left = 0
right = 0
result = 0
checkSum = set()
flag = set()
checkSum.add(inputData[0][1])

while True:
    tmpLen = inputData[right][0] - inputData[left][0]

    if tmpLen > d:
        if inputData[left][1] in flag:
            flag.remove(inputData[left][1])
        if inputData[left][1] in checkSum:
            checkSum.remove(inputData[left][1])
        left += 1

    else:
        result = max(result, len(flag))
        right += 1
        if right == 2 * N: break

        if inputData[right][1] in checkSum:
            checkSum.remove(inputData[right][1])
            flag.add(inputData[right][1])
        else:
            checkSum.add(inputData[right][1])

print(result)
