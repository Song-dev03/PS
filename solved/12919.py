
def possible(sec, result):
    # print(sec)
    if result == sec:
        return True
    
    if len(result) < len(sec):
        return False
    
    res = False
    
    # 마지막이 A → 제거
    if result[-1] == 'A':
        res |= possible(sec, result[:-1])
    
    # 처음이 B → 제거 후 뒤집기
    if result[0] == 'B':
        res |= possible(sec, result[1:][::-1])
    
    return res

S = input()
T = input()

print(1 if possible(S,T) else 0)