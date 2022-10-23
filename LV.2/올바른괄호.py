def solution(s):
    x = 0
    for i in s:
        if x < 0:
            break
        if i == '(':
            x += 1
        elif i == ')':
            x -= 1
    if x == 0:
        return True
    else:
        return False