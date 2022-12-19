def solution(s):
    answer = 0
    count = 0

    for x in range(len(s) - 2):
        if s[x] == s[x + 1] == s[x + 2] and int(s[x: x + 3]) >= answer:
            answer = int(s[x: x + 3])
            count += 1

    if (count == 0): answer = -1

    return answer


print(solution("000"))
