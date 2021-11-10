# https://www.acmicpc.net/problem/14173

A = list(map(int,input().split()))

B = list(map(int,input().split()))

X_startPoint = min(A[0],B[0])
Y_startPoint = min(A[1],B[1])

X_endPoint = max(A[2],B[2])
Y_endPoint = max(A[3],B[3])

result = max((Y_endPoint-Y_startPoint), (X_endPoint-X_startPoint))
print(result*result)