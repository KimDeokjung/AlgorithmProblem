#https://www.acmicpc.net/problem/9184

result_record = {}

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if (20, 20, 20) in result_record:
            return result_record[(20, 20, 20)]
        else:
            result = w(20, 20, 20)
            result_record[(20, 20, 20)] = result
            return result
    if a < b < c:
        if (a, b, c) in result_record:
            return result_record[(a, b, c)]
        else:
            N = M = O = 0
            if(a, b, c-1) in result_record:
                N = result_record[(a, b, c-1)]
            else:
                N = w(a, b, c-1)
                result_record[(a, b, c-1)] = N
            if(a, b-1, c-1) in result_record:
                M = result_record[(a, b-1, c-1)]
            else:
                M = w(a, b-1, c-1)
                result_record[(a, b-1, c-1)] = M
            if(a, b-1, c) in result_record:
                O = result_record[(a, b-1, c)]
            else:
                O = w(a, b-1, c)
                result_record[(a, b-1, c)] = O
            return N + M - O
    N = M = O = P = 0
    if (a-1, b, c) in result_record:
        N = result_record[(a-1, b, c)]
    else:
        N = w(a-1, b, c)
        result_record[(a-1, b, c)] = N
    if (a-1, b-1, c) in result_record:
        M = result_record[(a-1, b-1, c)]
    else:
        M = w(a-1, b-1, c)
        result_record[(a-1, b-1, c)] = M
    if (a-1, b, c-1) in result_record:
        O = result_record[(a-1, b, c-1)]
    else:
        O = w(a-1, b, c-1)
        result_record[(a-1, b, c-1)] = O
    if (a-1, b-1, c-1) in result_record:
        P = result_record[(a-1, b-1, c-1)]
    else:
        P = w(a-1, b-1, c-1)
        result_record[(a-1, b-1, c-1)] = P
    return N + M + O - P

while True:
    a, b, c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')
