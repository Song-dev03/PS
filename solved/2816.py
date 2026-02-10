n = int(input())
list = []
com_list = []
for i in range(0,n):
    list.append(input())
tar = 0
while list[tar] != "KBS1":
    com_list.append('1')
    tar = tar+1
while tar != 0:
    com_list.append('4')
    x = list[tar]
    list[tar] = list[tar-1]
    list[tar-1] = x
    tar = tar-1
while list[tar] != "KBS2":
    com_list.append('1')
    tar = tar+1
while tar != 1:
    com_list.append('4')
    x = list[tar]
    list[tar] = list[tar-1]
    list[tar-1] = x
    tar = tar-1
print(''.join(com_list))