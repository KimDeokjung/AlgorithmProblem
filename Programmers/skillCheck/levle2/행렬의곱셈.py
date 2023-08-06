def solution(arr1, arr2):
    n = len(arr1)
    n2 = len(arr1[0])
    m = len(arr2)
    m2 = len(arr2[0])

    answer = [[0 for x in range(m2)] for y in range(n)]

    for x in range(n):
        for y in range(m2):
            tmp = 0
            for z in range(m):
                tmp += arr1[x][z] * arr2[z][y]
            answer[x][y] = tmp

    return answer

