import math
n, m = map(int, input().split(":"))
flag = math.gcd(n, m)
print(n//flag, end="")
print(":", end="")
print(m//flag, end="")