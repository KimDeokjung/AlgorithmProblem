# https://www.acmicpc.net/problem/8718

a,b=map(int,input().split())
c=print
if b*7<=a:c(b*7000)
elif b*3.5<=a:c(b*3500)
elif b*7/4<=a:c(b*1750)
else:c(0)