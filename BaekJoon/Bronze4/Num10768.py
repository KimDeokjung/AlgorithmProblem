# https://www.acmicpc.net/problem/10768

Month = int(input())
Day = int(input())

if Month*100 + Day < 218:print("Before")
elif Month*100 + Day > 218:print("After")
else:print("Special")
