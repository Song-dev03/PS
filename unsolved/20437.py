T = int(input())

def get_chr_count(tar):
    chr_count_list = [0] * 26
    for c in tar:
        chr_count_list[ord(c) - ord('a')] += 1
    return chr_count_list

while T>0:
    W = input()
    k = int(input())
    for window_size in range(k,len(W)+1):
        for i in range(0, len(W)-window_size):
            tar = W[i:i+window_size]
            if k in get_chr_count(tar):
                break
        else:
            continue
        break
    if window_size == len(W) and k not in get_chr_count(W):
        print(-1)
        T-=1
        continue
    else:
        print(window_size, end=' ')
    
    for window_size in range(len(W),k-1,-1):
        for i in range(0, len(W)-window_size):
            tar = W[i:i+window_size]
            if tar[0] == tar[-1] and get_chr_count(tar)[ord(tar[0])-ord('a')] == k:
                break
        else:
            continue
        break
    if window_size == k and (tar[0] != tar[-1] or get_chr_count(tar)[ord(tar[0])-ord('a')] != k):
        print(-1)
    else:
        print(window_size)
    T-=1