import sys
input = sys.stdin.readline

def roundFuc(n):
    return int(n) + 1 if n - int(n) >= 0.5 else int(n)

result = 0
n = int(input())

inputData = dict()
for x in range(1, 31):
    inputData[x] = 0

for x in range(n):
    inputData[int(input())] += 1

rightFlag = leftFlag = flag = roundFuc(n * 0.15)
checkSum = 1
while True:
    if inputData[checkSum] >= leftFlag:
        inputData[checkSum] -= leftFlag
        break
    else:
        leftFlag -= inputData[checkSum]
        inputData[checkSum] = 0
        checkSum += 1

checkSum = 30
while True:
    if inputData[checkSum] >= rightFlag:
        inputData[checkSum] -= rightFlag
        break
    else:
        rightFlag -= inputData[checkSum]
        inputData[checkSum] = 0
        checkSum -= 1

result = 0
for x in range(1, 31):
    result += (x * inputData[x])

if n == 0: print(0)
else: print(roundFuc(result / (n - (flag * 2))))