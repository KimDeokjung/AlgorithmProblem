checkSum = dict()

def getNum(n, k):
    if n * 100 + k in checkSum:
        return checkSum[n * 100 + k]

    if n == k or k == 1: return 1
    else:
        tmp = getNum(n - 1, k - 1) + getNum(n - 1, k)
        checkSum[n * 100 + k] = tmp
        return tmp


n, k = map(int, input().split())
print(getNum(n, k))