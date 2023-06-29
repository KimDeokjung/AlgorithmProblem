N = int(input())

chessBoard = [-1 for _ in range(N)]

def abc(board, depth):
    if depth == N:
        return 1

    result = 0
    checkFlag = -1
    for x in range(N):
        if board[x] != -1: continue

        flag = True
        for y in range(N):
            if abs(x - y) <= depth and board[y] == abs(depth - abs(x - y)): flag = False

        if depth == N - 1 and flag:
            result += 1
            board[x] = -1
        elif flag:
            if checkFlag != -1:
                board[checkFlag] = -1
            board[x] = depth
            checkFlag = x
            result += abc(board, depth + 1)
            board[x] = -1

    return result

result = 0
for x in range(N):
    chessBoard[x - 1] = -1
    chessBoard[x] = 0

    result += abc(chessBoard, 1)

print(result)