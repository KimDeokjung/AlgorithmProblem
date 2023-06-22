def solution(S):
    inputData = list(S)
    result = 0

    for x in range(len(S)):
        if inputData[0] == inputData[-1]: result += 1
        inputData.append(inputData.pop(0))

    return result

def solution2(S):
    result = 0

    for x in range(-1, len(S) - 1):
        if S[x] == S[x + 1]: result += 1

    return result

