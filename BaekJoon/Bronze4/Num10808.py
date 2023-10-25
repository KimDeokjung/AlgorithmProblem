result = [0 for _ in range(26)]
# print(result)

for x in input():
    # print(ord(x) - 97)
    result[ord(x) - 97] += 1

print(* result)