# https://www.acmicpc.net/problem/5575

a=[]
for x in range(3):a.append(list(map(int,input().split())))
for x in a:b=x[5]-x[2];c=x[4]-x[1]+b//60;print((x[3]-x[0]+c//60)%24,c%60,b%60)
