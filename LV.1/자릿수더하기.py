def solution(n):
    n = str(n)
    sum = 0
    for i in n:
        i = int(i)
        sum = sum + i
    return sum


'''
def solution(n):
    return sum([int(i) for i in str(n)])
'''