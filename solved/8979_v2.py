n, k = map(int, input().split())
county_list = []
rank_list = {}

def isHigherRank(a,b):
    if county_list[b][1] >= county_list[a][1]:
        if county_list[b][1] > county_list[a][1]:
            return True
        elif county_list[b][2] >= county_list[a][2]:
            if county_list[b][2] > county_list[a][2]:
                return True
            elif county_list[b][3] > county_list[a][3]:
                return True
            else:
                return False
        else:
            return False
    return False

for i in range(n):
    a  = tuple(map(int, input().split()))
    county_list.append(a)

for i in range(n):
    for j in range(n-i-1):
        if isHigherRank(j,j+1):
            tmp = county_list[j+1]
            county_list[j+1] = county_list[j]
            county_list[j] = tmp
    

rank = 0
tmp = 1
for i in range(n):
    rank_list[county_list[i][0]] = rank+1
    if i<n-1 and county_list[i][1:4] == county_list[i+1][1:4]:
        tmp = tmp + 1
    else:
        rank = rank + tmp
        tmp = 1

# for i in range(n):
#     print(county_list[i])

print(rank_list[k])