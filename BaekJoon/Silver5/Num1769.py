X = input()
result = 0

while len(X) > 1:
    result += 1
    tmp = 0
    for y in X:
        tmp += int(y)
    X = str(tmp)

print(result)
print(["YES", "NO"][int(X) % 3 != 0])
