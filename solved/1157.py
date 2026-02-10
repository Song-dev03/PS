s = input()
gap = ord('a')-ord('A')
cnt = [0 for i in range(100)]
for i in range(0,len(s)):
    tar = ord(s[i]) if ord(s[i])<92 else ord(s[i])-gap
    cnt[tar] = cnt[tar] + 1

max_cnt = max(cnt)
ans = ' '
for i in range(65,ord('Z')+1,1):
    if max_cnt == cnt[i]:
        if ans == ' ':
            ans = chr(i)
        else:
            ans = '?'
print(ans)