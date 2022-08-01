def isrange(top_point, low_point, target):
    return top_point[0] <= target[0] <= low_point[0] and top_point[1] <= target[1] <= low_point[1]


def solution(board, skill):
    answer = 0
    len_x = len(board)
    len_y = len(board[0])

    for x in range(len_x):
        for y in range(len_y):
            damage = 0
            for z in skill:
                if z[0] == 1:
                    if isrange(z[1:3], z[3:5], [x, y]):
                        damage += z[5]
                else:
                    if isrange(z[1:3], z[3:5], [x, y]):
                        damage -= z[5]
            if damage >= board[x][y]:
                answer += 1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))