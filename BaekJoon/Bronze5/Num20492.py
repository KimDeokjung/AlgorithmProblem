## https://www.acmicpc.net/problem/20492

# a=int(input())//250
# print(a*195,a*239)

for x in range(2,239):
    if 195%x == 0 and 239%x == 0:
        print(x)