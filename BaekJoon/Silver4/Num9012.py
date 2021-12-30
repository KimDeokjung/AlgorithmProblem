#https://www.acmicpc.net/problem/9012

N = int(input())
resultData = list()
for x in range(N):
    inputData = input()
    checkData = 0
    for y in range(len(inputData)):
        if inputData[y] == '(':checkData+=1
        else:checkData-=1

        if checkData < 0:
            resultData.append('NO')
            break
    else:
        if checkData == 0:resultData.append("YES")
        else:resultData.append("NO")

print(*resultData)