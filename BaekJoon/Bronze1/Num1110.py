# https://www.acmicpc.net/problem/1110

num = int(input())
nextNum = 0
target = num
result = 0

while target != nextNum:
    result += 1
    pre_num = num // 10
    pro_num = num % 10
    nextNum = pre_num + pro_num
    nextNum = pro_num * 10 + nextNum % 10
    num = nextNum

print(result)
