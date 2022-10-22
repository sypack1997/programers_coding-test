def solution(a, b):
    sum = 0
    if b > a:
        for i in range(a,b+1):
            sum+=i
    else:
        for i in range(b, a+1):
            sum+=i
    return sum

'''
def solution(a,b):
    if a>b:
        a,b = b,a
    return sum(range(a,b+1))
'''