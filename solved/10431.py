T = int(input())

for test_case in range(T):
    x = input().split()
    li = list(map(int, x[1:21]))
    cnt = 0
    for i in range(0,20):
        for j in range(0,i+1):
            if li[j] > li[i]:
                tar = li[i]
                li[j+1:i+1] = li[j:i]
                cnt = cnt + i - j
                li[j] = tar
                break
    print(test_case+1, cnt)