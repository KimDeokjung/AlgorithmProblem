import sys
sys.setrecursionlimit(2000000)

def nextStep(checkSum, flag, xP, yP, value, N):
    if xP + flag[0] < 0 or xP + flag[0] >= N or yP + flag[1] < 0 or yP + flag[1] >= N or checkSum[xP + flag[0]][yP + flag[1]] != 0:
        if flag[0] == 1 and flag[1] == 0:
            flag = [0, 1]
            if checkSum[xP + flag[0]][yP + flag[1]] != 0: return
            nextStep(checkSum, flag, xP, yP, value, N)
        elif flag[0] == 0 and flag[1] == 1:
            flag = [-1, -1]
            if checkSum[xP + flag[0]][yP + flag[1]] != 0: return
            nextStep(checkSum, flag, xP, yP, value, N)
        else:
            flag = [1, 0]
            if checkSum[xP + flag[0]][yP + flag[1]] != 0: return
            nextStep(checkSum, flag, xP, yP, value, N)

    xP += flag[0]
    yP += flag[1]
    checkSum[xP][yP] = value
    value += 1
    nextStep(checkSum, flag, xP, yP, value, N)

def solution(n):
    if n == 1: return [1]
    checkSum = [[0 for _ in range(n)] for __ in range(n)]
    answer = []
    checkSum[0][0] = 1
    nextStep(checkSum, [1, 0], 0, 0, 2, n)
    for x in range(n):
        for y in range(n):
            if checkSum[x][y] == 0: break
            answer.append(checkSum[x][y])

    return answer


print(solution(1))