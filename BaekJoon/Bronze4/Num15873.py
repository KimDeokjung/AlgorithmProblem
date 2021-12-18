# https://www.acmicpc.net/problem/15873

inputData = input()
if len(inputData) == 4:print(20)
elif len(inputData) == 3:
    if inputData[1] == '0':print(int(inputData[:2]) + int(inputData[2]))
    else:print(10 + int(inputData[0]))
else:print(int(inputData[0]) + int(inputData[1]))