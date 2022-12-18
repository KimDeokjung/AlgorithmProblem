num = int(input())
data = {}
result = 0

for x in range(num):
    startP, endP = map(int, input().split())
    data[startP] = endP

sort_data = sorted(data.keys())
left = sort_data[0]
right = data[sort_data[0]]

for x in range(len(sort_data) - 1):
    if right >= sort_data[x + 1]:
        right = max(data[sort_data[x + 1]], right)
    else:
        result += right - left
        left = sort_data[x + 1]
        right = data[sort_data[x + 1]]

result += right - left

print(result)
