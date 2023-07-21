N = int(input())
inputData = list(map(int, input().split()))
sorted(inputData)

result = [0, 0]
resultNum = 2000000001
start = 0
end = len(inputData) - 1

while start != end:
    tmp = inputData[start] + inputData[end]
    if resultNum > abs(tmp):
        resultNum = abs(tmp)
        result[0] = inputData[start]
        result[1] = inputData[end]

    if abs(inputData[start] + inputData[end - 1]) < abs(inputData[start + 1] + inputData[end]): end -= 1
    else: start += 1

sorted(result)
print(*result)