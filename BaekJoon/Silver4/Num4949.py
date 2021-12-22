#https://www.acmicpc.net/problem/4949

inputData = list()
result = list()

while True:
    data = input()
    if data == ".":break
    inputData.append(data)

for x in inputData:
    smallParenthesis = 0
    bigParenthesis = 0
    stackData = list()

    for y in range(len(x)):
        if x[y] == '(':
            stackData.append('(')
            smallParenthesis += 1
        elif x[y] == ')':
            if len(stackData) == 0:
                result.append('no')
                break
            checksum = stackData.pop()
            if checksum != '(':
                result.append('no')
                break
            smallParenthesis -= 1
        elif x[y] == '[':
            stackData.append('[')
            bigParenthesis += 1
        elif x[y] == ']':
            if len(stackData) == 0:
                result.append('no')
                break
            checksum = stackData.pop()
            if checksum != '[':
                result.append('no')
                break
            bigParenthesis -= 1

        if smallParenthesis < 0 or bigParenthesis < 0:
            result.append('no')
            break
    else:
        if smallParenthesis != 0 or bigParenthesis != 0:
            result.append('no')
        else:
            result.append('yes')

print(*result)

