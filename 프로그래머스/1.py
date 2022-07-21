def solution(grade):
    origin = sum(grade)

    for x in range(1, len(grade) + 1):
        grade[len(grade) - x:] = checkGrade(grade[len(grade) - x:])

    result = sum(grade)

    return origin - result

def checkGrade(grade):
    for x in range(len(grade) - 1):
        if grade[x + 1] < grade[x]:
            grade[x] = grade[x + 1]
    return grade

print(solution([3, 2, 1]))