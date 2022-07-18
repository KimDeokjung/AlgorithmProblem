#https://www.acmicpc.net/problem/11723
from sys import stdin

data = [0] * 20
N = int(input())

for x in range(N):
    line = stdin.readline()[:-1]
    if line == "all":
        data = [1] * 20
    elif line == "empty":
        data = [0] * 20
    else:
        command, a = line.split()
        a = int(a) - 1
        if command == "add":
            data[a] = 1
        if command == "check":
            print(int(data[a] != 0))
        if command == "toggle":
            data[a] = int(data[a] == 0)
        elif command == "remove":
            data[a] = 0

