N, S = map(int, input().split())

inputData = list(map(int, input().split()))
result = 0
checkSum = left = right = 0

while right <= N or left <= N:
    if checkSum < S:
        if right == N:
            break
        else:
            checkSum += inputData[right]
            right += 1
    else:
        if left == N:
            break
        if result == 0:
            result = right - left
        else:
            result = min(result, right - left)
        checkSum -= inputData[left]
        left += 1

if checkSum >= S:
    if result == 0:
        result = right - left
    else:
        result = min(result, right - left)

if S == 0:
    print(1)
else:
    print(result)