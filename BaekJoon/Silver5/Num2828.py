N, M = map(int, input().split())

result = 0
left = 1
right = left + M - 1
for _ in range(int(input())):
    x = int(input())

    if left <= x <= right:
        pass
    elif x < left:
        result += (left - x)
        right -= (left - x)
        left = x
    else:
        result += (x - right)
        left += (x - right)
        right = x

print(result)