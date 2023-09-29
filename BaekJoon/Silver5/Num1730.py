N = int(input())
inputData = [[0 for _ in range(N)] for __ in range(N)]
result = [["." for _ in range(N)] for __ in range(N)]

x = y = 0
inputData[x][y] = 1
for z in input():
    if z == "D":
        if x == N-1: continue
        if result[x][y] == ".":
            result[x][y] = "|"
        elif result[x][y] == "-":
            result[x][y] = "+"

        if result[x + 1][y] == ".":
            result[x + 1][y] = "|"
        elif result[x + 1][y] == "-":
            result[x + 1][y] = "+"
        x += 1
    elif z == "U":
        if x == 0: continue
        if result[x][y] == ".":
            result[x][y] = "|"
        elif result[x][y] == "-":
            result[x][y] = "+"

        if result[x - 1][y] == ".":
            result[x - 1][y] = "|"
        elif result[x - 1][y] == "-":
            result[x - 1][y] = "+"
        x -= 1
    elif z == "R":
        if y == N - 1: continue
        if result[x][y] == ".":
            result[x][y] = "-"
        elif result[x][y] == "|":
            result[x][y] = "+"

        if result[x][y + 1] == ".":
            result[x][y + 1] = "-"
        elif result[x][y + 1] == "|":
            result[x][y + 1] = "+"
        y += 1
    elif z == "L":
        if y == 0: continue
        if result[x][y] == ".":
            result[x][y] = "-"
        elif result[x][y] == "|":
            result[x][y] = "+"

        if result[x][y - 1] == ".":
            result[x][y - 1] = "-"
        elif result[x][y - 1] == "|":
            result[x][y - 1] = "+"
        y -= 1

for x in result:
    print("".join(x))