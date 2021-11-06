# https://www.acmicpc.net/problem/11943

firstBasket = list(map(int,input().split()))
secondBasket = list(map(int, input().split()))

print(min(firstBasket[0] + secondBasket[1], firstBasket[1]+ secondBasket[0]))
