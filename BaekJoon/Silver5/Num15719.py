import sys
N = int(input())
a = N * (N - 1) // 2
inputData = sys.stdin.readline().rstrip()
tmp = 0
t = ""
for x in inputData:
    if x.isdigit():
        t += x
    else:
        tmp += int(t)
        t = ""
tmp += int(t)
print(tmp - a)