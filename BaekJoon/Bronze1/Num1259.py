#https://www.acmicpc.net/problem/1157

resultList = list()

while True:
    inputData = input()
    if inputData == '0':
        break
    for x in range(len(inputData) // 2):
        if inputData[x] != inputData[-(x + 1)]:
            resultList.append('no')
            break
    else:
        resultList.append('yes')

print(*resultList)