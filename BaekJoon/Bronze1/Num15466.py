T = int(input())

result = list()

for _ in range(T):
    input()
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    nowResult =  len(A.intersection(B)) / len(A.union(B))

    if nowResult > 0.5: result.append(1)
    else: result.append(0)

print(*result)
