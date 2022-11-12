def solution(n):
    ftr = 2
    ftr_list = [0, 1, 2]
    for i in range(3, 11):
        ftr = ftr * i
        ftr_list.append(ftr)
        
    for j in range(len(ftr_list)+1):
        if ftr_list[j] < n < ftr_list[j+1]:
            return j
        elif n == ftr_list[j]:
            return j

'''
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k
'''


'''
def solution(n):
    base , n = 1, 1
    while base <= n:
        m += 1
        base *= m
    return m-1
'''