test = [0 for x in range(100)]

def abc(board, x):
    board[x] = x

for x in range(100):
    abc(test, x)

print(test)