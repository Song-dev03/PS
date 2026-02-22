n = int(input())

body_list = []
rank_list = []

for i in range(n):
    x = tuple(map(int, input().split()))
    body_list.append(x)

for i in range(n):
    rank = 1
    for j in range(n):
        if body_list[j][0] > body_list[i][0] and body_list[j][1] > body_list[i][1]:
            rank = rank+1
    rank_list.append(rank)


for i in range(n):
    print(rank_list[i], end = " ")
print()