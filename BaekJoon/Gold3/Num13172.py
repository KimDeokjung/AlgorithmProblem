import math
import sys
input = sys.stdin.readline

result = 0
modNum = 1000000007
checkSum = dict()

for _ in range(int(input())):
    parents, child = map(int, input().split())

    gcd = math.gcd(parents, child)
    parents //= gcd
    child //= gcd

    if parents == 1:
        result += child
        continue

    reverseParents = 0
    if parents in checkSum:
        reverseParents = checkSum[parents]
    else:
        reverseParents = pow(parents, -1, modNum)
        checkSum[parents] = reverseParents
    result += reverseParents * child
    result %= modNum

print(result)
