H, W, N, M = map(int, input().split())

a = 0
b = 0
for i in range(0,H,N+1):
    a = a+1
for j in range(0,W,M+1):
    b = b+1
print(a*b)