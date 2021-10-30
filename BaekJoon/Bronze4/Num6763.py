# https://www.acmicpc.net/problem/6763

a=-int(input())+int(input())
print(['Congratulations, you are within the speed limit!',f"You are speeding and your fine is ${[100,[500,270][a<31]][a>20]}."][a>0])
