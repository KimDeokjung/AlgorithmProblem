T = int(input())
inputData = list()

for x in range(T):
    num1, num2 = map(int, input().split())
    print(f'Case #{x + 1}: {num1} + {num2} = {num1 + num2}')
