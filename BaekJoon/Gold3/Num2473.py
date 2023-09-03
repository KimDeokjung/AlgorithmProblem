N = int(input())
inputData = list(map(int, input().split()))

inputData.sort()

result = [abs(inputData[0] + inputData[1] + inputData[2]), 0, 1, 2]

for index, target in enumerate(inputData[:-2]):

    left = index + 1
    right = N - 1
    tmp = inputData[left] + inputData[right]

    while True:
        if left == right: break
        if abs(tmp + target) < result[0]:
            result = [abs(tmp + target), index, left, right]

        if tmp > -target:
            tmp -= inputData[right]
            right -= 1
            tmp += inputData[right]
        else:
            tmp -= inputData[left]
            left += 1
            tmp += inputData[left]

result[1] = inputData[result[1]]
result[2] = inputData[result[2]]
result[3] = inputData[result[3]]

print(*result[1:])