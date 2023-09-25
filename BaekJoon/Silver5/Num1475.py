N = input()

inputData = [0 for _ in range(9)]

for x in N:
    tmp = int(x)
    if tmp == 9:
        tmp = 6

    inputData[tmp] += 1

inputData[6] = inputData[6] // 2 + inputData[6] % 2

print(max(inputData))