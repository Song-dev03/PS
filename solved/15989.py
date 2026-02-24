dt = [0] * 10001

T = int(input())

for i in range(10001):
    dt[i] = 1
for i in range(2,10001):
    dt[i] = dt[i] + dt[i-2]
for i in range(3,10001):
    dt[i] = dt[i] + dt[i-3]

for i in range(T):
    n = int(input())
    print(dt[n])