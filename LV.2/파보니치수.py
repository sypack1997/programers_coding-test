def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a % 1234567


'''
def solution(n):
    sum_list = [0, 1]
    
    for i in range(n):
        sum_list.append(sum_list[i] + sum_list[i+1])
        
    return sum_list % 1234567
'''