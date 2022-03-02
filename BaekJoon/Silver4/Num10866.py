# https://www.acmicpc.net/problem/10866

N = int(input())
result = list()
Deque = list()

for x in range(N):
    command = input().split()
    if command[0] == "push_front":
        Deque.insert(0, command[1])
    elif command[0] == "push_back":
        Deque.append(command[1])
    elif command[0] == "pop_front":
        if len(Deque):result.append(Deque.pop(0))
        else:result.append(-1)
    elif command[0] == "pop_back":
        if len(Deque):result.append(Deque.pop(-1))
        else:result.append(-1)
    elif command[0] == "size":
        result.append(len(Deque))
    elif command[0] == "empty":
        if len(Deque):result.append(0)
        else:result.append(1)
    elif command[0] == "front":
        if len(Deque):result.append(Deque[0])
        else:result.append(-1)
    elif command[0] == "back":
        if len(Deque):result.append(Deque[-1])
        else:result.append(-1)

print(*result)