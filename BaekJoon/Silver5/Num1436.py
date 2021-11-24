# https://www.acmicpc.net/problem/1436

num = int(input())
check = 0
while True:
    check += 1
    if str(check).find('666')>-1:
        num -= 1
    if num==0:print(check);break;