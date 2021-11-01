# https://www.acmicpc.net/problem/10039

score = []
for _ in range(5):score.append(max(int(input()),40))
print(sum(score)//5)
