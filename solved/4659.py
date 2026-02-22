pw = input()
odd = ["a", "e", "i", "u", "o"]

while pw != "end":
    even_cnt = 0
    odd_cnt = 0
    total_odd_cnt = 0
    pass_fail = ""
    for i in range(len(pw)):
        if pw[i] in odd:
            if odd_cnt == 2:
                pass_fail=" not"
                break
            odd_cnt = odd_cnt + 1
            even_cnt = 0
            total_odd_cnt = total_odd_cnt + 1
        else:
            if even_cnt == 2:
                pass_fail=" not"
                break
            even_cnt = even_cnt + 1
            odd_cnt = 0
        
        if i > 0 and pw[i] == pw[i-1] and pw[i]!="e" and pw[i] !="o":
            pass_fail = " not"

    if total_odd_cnt == 0:
        pass_fail = " not"

    print("<"+pw+">"+" is"+pass_fail+" acceptable.")
    pw = input()