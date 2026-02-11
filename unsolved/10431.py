T = int(input())

for _ in range(T):
    x = input().split()
    li = x[1:21]
    cnt = 0
    for i in range(0,20):
        for j in range(0,i+1):
            if li[j] > li[i]:
                tar = li[i]
                for k in range(j+1,i+1):
                    li[k] = li[k-1]
                    cnt = cnt +1
                li[j] = tar
            break
    print(cnt)