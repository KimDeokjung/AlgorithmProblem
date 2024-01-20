checkSum = dict()

def checkResult(first, second, depth):
    if first - second < 0: return depth + 1
    elif (first * 40000 + second) in checkSum:
        return checkSum[(first * 40000 + second)] + depth - 1
    else:
        nowResult = checkResult(second, first - second, depth + 1)
        checkSum[(first * 40000 + second)] = nowResult
        return nowResult

N = int(input())
maxResult = 0
flag = 0

for x in range(N+1):
    tmp = checkResult(N, x, 1)
    if tmp > maxResult:
        maxResult = tmp
        flag = x

print(maxResult)
print(N, end=" ")
print(flag, end=" ")
while True:
    N -= flag
    N, flag = flag, N
    if flag < 0: break
    else: print(flag, end=" ")
