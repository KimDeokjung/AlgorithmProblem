# https://www.acmicpc.net/problem/2588

a=int(input())
b=int(input())
print(b%10*a,b//10%10*a,b//100*a,a*b)
