#https://www.acmicpc.net/problem/2884

a,b=map(int,input().split())
print((a-(b<45))%24,(b-45)%60)
