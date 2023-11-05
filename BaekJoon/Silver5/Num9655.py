N = int(input())

checkSum = [0 for _ in range(1001)]
checkSum[0] = 1
checkSum[1] = 0
checkSum[2] = 1

for x in range(4, N + 1):
    if checkSum[x - 1] == 1 or checkSum[x - 3] == 1: checkSum[x] = 0
    else: checkSum[x] = 1

if checkSum[N] == 0: print("SK")
else: print("CY")
