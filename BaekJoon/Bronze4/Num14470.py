# https://www.acmicpc.net/problem/14470

C = int(input())
target = int(input())
iceUp = int(input())
dry = int(input())
normalUp = int(input())

result = 0

if C < 1:
    result += dry
    result += -C * iceUp
    result += target * normalUp
else:
    result += (target - C) * normalUp

print(result)