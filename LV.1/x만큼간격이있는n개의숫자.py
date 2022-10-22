def solution(x, n):
    x_list = []
    for i in range(1, n+1):
        x_list.append(x*i)
    return x_list


'''
def solution(x,n):
    return [x*n+n for i in range(n)]
'''