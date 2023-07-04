first = input()
second = input()
checkSum = [0 for _ in range(len(first))]
result = 0

for x in second:
    flag = 0
    for index, y in enumerate(first):
        if flag < checkSum[index]:
            flag = checkSum[index]
        elif x == y:
            checkSum[index] = flag + 1
            result = max(flag + 1, result)

print(result)

