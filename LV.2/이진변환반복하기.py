def solution(s):
    cnt_zero = 0
    cnt = 0
    while s != '1':
        s = str(s)
        if '0' in s:
            cnt_zero += s.count('0')
            s = s.replace('0', '')
        
        s_length = len(s)
        s = bin(s_length)[2:]
        cnt += 1
    return [cnt, cnt_zero]