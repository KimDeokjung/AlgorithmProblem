def solution(sequence, k):
    lenSeq = len(sequence)
    resultL = 0
    resultR = 0
    resultLen = 1000001

    left = 0
    right = 0
    flag = 0

    while True:
        if flag > k:
            if left >= lenSeq: break
            flag -= sequence[left]
            left += 1
        elif flag < k:
            if right >= lenSeq: break
            flag += sequence[right]
            right += 1
        else:
            if right - left < resultLen:
                resultL = left
                resultR = right - 1
                resultLen = right - left
            if right >= lenSeq: break
            flag += sequence[right]
            right += 1

    answer = [resultL, resultR]
    return answer


s = [2, 2, 2, 2, 2]
k = 10
print(solution(s, k))