def solution(board):
    xCount = 0
    oCount = 0
    xWin = False
    oWin = False

    for x in range(3):
        for y in range(3):
            if board[x][y] == "X": xCount += 1
            elif board[x][y] == "O": oCount += 1

    for x in range(3):
        if "X" == board[x][0] == board[x][1] == board[x][2]: xWin = True
        if "X" == board[0][x] == board[1][x] == board[2][x]: xWin = True

        if "O" == board[x][0] == board[x][1] == board[x][2]: oWin = True
        if "O" == board[0][x] == board[1][x] == board[2][x]: oWin = True

    if "X" == board[0][0] == board[1][1] == board[2][2]: xWin = True
    if "X" == board[2][0] == board[1][1] == board[0][2]: xWin = True
    if "O" == board[0][0] == board[1][1] == board[2][2]: oWin = True
    if "O" == board[2][0] == board[1][1] == board[0][2]: oWin = True

    if xCount > oCount or oCount - xCount > 1 or (xWin and oWin): return 0
    if oWin and oCount - xCount != 1: return 0
    if xWin and oCount - xCount != 0: return 0

    return 1

board = ["...", "...", "..."]

print(solution(board))