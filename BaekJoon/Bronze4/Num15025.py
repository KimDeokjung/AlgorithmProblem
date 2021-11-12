# https://www.acmicpc.net/problem/15025

a=eval(input().replace(" ","+"))
if a==0:print("Not a moose")
elif a%2<1:print(f"Even {a}")
else:print(f"Odd {a+1}")
