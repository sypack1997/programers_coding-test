def solution(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum = sum + i
    return sum


'''
def solution(n):
    return n + sum([i for i in range(1,(n // 2) + 1 ) if num % 1 == 0])
'''


'''
def solutrion(n):
    return sum(filter(lambda x : num % x == 0, range(1, num + 1)))
'''