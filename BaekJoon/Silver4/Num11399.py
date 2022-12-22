N = int(input())
P = list(map(int, input().split()))

result = 0
total_sum = 0

for x in sorted(P):
    total_sum += x
    result += total_sum

print(result)