# https://www.acmicpc.net/problem/10703

inputData = list()
for _ in range(5):
    inputData.append(int(input()))

print(min(inputData[0]*inputData[4] , inputData[1] + inputData[3]*max(0,inputData[4] - inputData[2])))