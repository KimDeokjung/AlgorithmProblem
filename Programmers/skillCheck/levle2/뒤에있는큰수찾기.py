def findIndx(checkSum, data):
    left = -1
    right = len(checkSum)

    while left + 1 < right:
        mid = (left + right) // 2
        if checkSum[mid] <= data:
            left = mid
        else:
            right = mid

    return right

def solution(numbers):
    answer = []
    checkSum = sorted(numbers)

    for number in numbers:
        if number >= checkSum[-1]:
            answer.append(-1)
        else:
            answer.append(checkSum[findIndx(checkSum, number)])
    return answer


numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))