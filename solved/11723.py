n = int(input())
S = set()
result = []

while n>0:
    cmd = input().split()
    if len(cmd) == 2:
        comand, x = cmd
        x = int(x)
    else:
        comand = cmd[0]
    
    if comand == "add":
        S.add(x)
    elif comand == "remove":
        S.discard(x)
    elif comand == "check":
        result.append("1" if x in S else "0")
    elif comand == "toggle":
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    elif comand == "all":
        S = set(range(1,21))
    elif comand == "empty":
        S.clear()
    n = n-1

print("\n".join(result))