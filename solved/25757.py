n, K = input().split()
n = int(n)
# Y : 1, F : 2, O : 3
member_set = set()
if K == "Y":
    k = 1
elif K=="F":
    k = 2
else:
    k = 3
for i in range(n):
    x = input()
    member_set.add(x)

print(len(tuple(member_set))//k)