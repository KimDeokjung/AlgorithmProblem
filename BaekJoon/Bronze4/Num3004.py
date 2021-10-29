# https://www.acmicpc.net/problem/3004

a=int(input())+1
print(sum(range(a//2+1))*2+a%2*(a//2+1))