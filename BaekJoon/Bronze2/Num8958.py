#https://www.acmicpc.net/problem/8958

num = int(input())
result = list()
for x in range(num):
    target = input()
    point = 1
    target_score = 0
    for y in range(len(target)):
        if target[y] == "O":
            target_score += point
            point += 1
        else:point = 1
    result.append(target_score)
print(*result)