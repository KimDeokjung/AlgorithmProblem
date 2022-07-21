import sys
sys.setrecursionlimit(2500)
count = 0

def solution(rows, columns, lands):
    answer = [[0 for col in range(columns)] for row in range(rows)]

    for x in lands:answer[x[0] - 1][x[1] - 1] = 1

    ans = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(q, p):
        global count
        answer[q][p] = 1
        count += 1
        for t in range(4):
            ny = q + dy[t]
            nx = p + dx[t]
            if (0 <= ny < rows and 0 <= nx < columns and answer[ny][nx] == 4):
                dfs(ny, nx)

    for x in range(rows):
        extra_data = []
        flag = False
        for y in range(columns):
            if(flag):
                if answer[x][y] == 1:
                    for z in extra_data:
                        answer[x][z] += 2
                        extra_data = []
                else:extra_data.append(y)
            elif answer[x][y] == 1:
                flag = True

    for y in range(columns):
        extra_data = []
        flag = False
        for x in range(rows):
            if(flag):
                if answer[x][y] == 1:
                    for z in extra_data:
                        answer[z][y] += 2
                        extra_data = []
                else:extra_data.append(x)
            elif answer[x][y] == 1:
                flag = True

    for q in range(rows):
        for p in range(columns):
            if (answer[q][p] == 4):
                global count
                count = 0
                dfs(q, p)
                ans.append(count)

    if len(ans) == 0:result = [-1, -1]
    else:result = [min(ans), max(ans)]
    return result

print(solution(5,5,[]))