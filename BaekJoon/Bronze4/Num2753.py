# https://www.acmicpc.net/problem/2753

a=int(input())
print([0,1][(a%4==0and a%100!=0)or a%400==0])