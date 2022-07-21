import sys
sys.setrecursionlimit(50000)
count = 0

def solution(rows, columns, lands):
    answer = [[0 for col in range(columns)] for row in range(rows)]
    ans = []

    for x in lands:answer[x[0] - 1][x[1] - 1] = 1

    def dfs(q, p):
        global count
        count += 1
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        answer[q][p] = 1

        for t in range(4):
            ny = q + dy[t]
            nx = p + dx[t]
            if (0 <= ny < rows and 0 <= nx < columns and answer[ny][nx] == 0):
                dfs(ny, nx)

    for q in range(rows):
        for p in range(columns):
            if (answer[q][p] == 0):
                global count
                count = 0
                dfs(q, p)
                ans.append(count)

    ans.pop(0)
    return [-1, -1] if len(ans) == 0 else [min(ans), max(ans)]
