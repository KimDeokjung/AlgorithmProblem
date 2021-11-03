# https://www.acmicpc.net/problem/10179

num = int(input())
result = list()
for x in range(num):
    original = float(input())
    result.append('${:.2f}'.format(round(original*0.8,2)))
print(*result)