# https://www.acmicpc.net/problem/14038


W=[]
for x in range(6):W.append(input())
num = W.count("W")
print([[[-1,3][num>0],2][num>2],1][num>4])