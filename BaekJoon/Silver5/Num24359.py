def abc(num, n):
    result = []

    for x in range(n):
        if num % 10 == 0:
            tmp = num % 10
            tmp2 = num // 10
            num = tmp * (10 ** (n - 1)) + tmp2
        else:
            tmp = num % 10
            tmp2 = num // 10
            num = tmp * (10 ** (n - 1)) + tmp2
            result.append(num)

    return result

a = input()
b = input()

print(max(abc(int(a), len(a))) - min(abc(int(b), len(b))))
