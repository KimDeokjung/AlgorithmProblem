N = int(input())

checkSum = [2]
def isSosu(num):
    if num % 2 == 0: return False

    for x in range(3, int(num**.5) + 1, 2):
        if num % x == 0: return False

    return True


for x in range(3, 10000):
    if isSosu(x):
        checkSum.append(x)

for x in range(len(checkSum)):
    if checkSum[x] * checkSum[x+1] > N:
        print(checkSum[x] * checkSum[x+1])
        break