n, k = map(int, input().split())
county_list = []
for i in range(n):
    a  = tuple(map(int, input().split()))
    county_list.append(a)

rank_list = {}
list_sorted_gold = sorted(county_list, key = lambda x : x[1], reverse = True)
s = 0
list_sorted_silver = list_sorted_gold
for i in range(n):
    if i < n-1 and list_sorted_gold[i][1]>list_sorted_gold[i+1][1]:
        list_sorted_silver[s:i+1] = sorted(list_sorted_gold[s:i+1], key = lambda x : x[2], reverse = True)
        s = i+1
    elif i == n-1:
        list_sorted_silver[s:i+1] = sorted(list_sorted_gold[s:i+1], key = lambda x : x[2], reverse = True)
print(list_sorted_silver)
final_list = list_sorted_silver
s = 0
for i in range(n):
    if i > 0 and list_sorted_silver[i][1] > list_sorted_silver[i-1][1]:
        s = i
    if i < n-1 and list_sorted_silver[i][1] == list_sorted_silver[i+1][1] and list_sorted_silver[i][2] > list_sorted_silver[i+1][2]:
        final_list[s:i+1] = sorted(list_sorted_silver[s:i+1], key = lambda x : x[3], reverse = True)
        s = i+1
    elif i == n-1:
        final_list[s:i+1] = sorted(list_sorted_silver[s:i+1], key = lambda x : x[3], reverse = True)
print(final_list)
rank = 0
tmp = 1
for i in range(n):
    rank_list[final_list[i][0]] = rank+1
    if i<n-1 and final_list[i][1:4] == final_list[i+1][1:4]:
        tmp = tmp + 1
        continue
    else:
        rank = rank + tmp
        tmp = 1

print(rank_list[k])