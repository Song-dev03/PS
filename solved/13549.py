ts = [-1] * 100001

n,k = map(int,input().split())
queue = list()

queue.append((n,0))
ts[n] = 0
while ts[k] == -1:
    a = queue.pop(0)
    x = a[0]
    t = a[1]
    ts[x] = t

    if x*2<=100000 and ts[x*2] == -1:
        queue.append((x*2,t))
    if x-1>=0 and ts[x-1] == -1:
        queue.append((x-1,t+1))
    if x+1<=100000 and ts[x+1] == -1:
        queue.append((x+1,t+1))

    # print(a)

print(ts[k])