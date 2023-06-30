N = int(input())
checkSum = [0]

def findIndex(data):
    left = 0
    right = len(checkSum) - 1
    middle = (left + right) // 2

    while left < right:
        if checkSum[middle] > data:
            right = middle - 1
        elif checkSum[middle] < data:
            left = middle + 1
        else:
            return middle
        middle = (left + right) // 2

    for x in range(middle, len(checkSum)):
        if checkSum[x] > data:
            return x - 1

    return middle

for x in list(map(int, input().split())):
    if x > checkSum[-1]:
        checkSum.append(x)
    elif x < checkSum[-1]:
        flag = findIndex(x)
        if flag == 0: flag = 1
        while True:
            if checkSum[flag - 1] == x:
                break
            if checkSum[flag] > x:
                checkSum[flag] = x
                break
            flag += 1

print(len(checkSum) - 1)