X = int(input())

result = 0

while X != 0:
    result += (X % 2)
    X //= 2

print(result)
