N, M = map(int, input().split())
inputData = list(map(int, input().split()))

left = 0
right = 0
result = 0
tmp = 0

while True:
    if tmp < M:
        if right >= N: break
        tmp += inputData[right]
        right += 1
    elif tmp > M:
        if left >= N: break
        tmp -= inputData[left]
        left += 1
    else:
        if left >= N: break
        result += 1
        tmp -= inputData[left]
        left += 1




print(result)