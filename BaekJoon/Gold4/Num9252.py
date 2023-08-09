import sys
input = sys.stdin.readline

first = list(input().rstrip())
second = list(input().rstrip())
lenFirst = len(first)
lenSecond = len(second)

checksum = [["" for _ in range(lenSecond + 1)] for __ in range(lenFirst + 1)]

for x in range(1, lenFirst + 1):
    for y in range(1, lenSecond + 1):
        if first[x - 1] == second[y - 1]:
            checksum[x][y] = checksum[x - 1][y - 1] + first[x - 1]
        else:
            if len(checksum[x - 1][y]) < len(checksum[x][y - 1]):
                checksum[x][y] = checksum[x][y - 1]
            else:
                checksum[x][y] = checksum[x - 1][y]

print(len(checksum[-1][-1]))
print(checksum[-1][-1])