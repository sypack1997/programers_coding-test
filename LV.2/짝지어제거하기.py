def solution(s):
    s_list = []
    
    for i in s:
        if len(s_list) == 0:
            s_list.append(i)
        elif i == s_list[-1]:
            s_list.pop()
        else:
            s_list.append(i)
    
    if len(s_list) > 0:
        return 0
    else:
        return 1