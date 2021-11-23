#https://www.acmicpc.net/problem/10871

num, target = map(int,input().split())
inputData = list(map(int,input().split()))
for x in range(num):
    if target > inputData[x]: print(inputData[x])