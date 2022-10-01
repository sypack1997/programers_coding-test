def solution(n):
    n = str(n)
    n_list = []
    for i in n[::-1]:
        n_list.append(int(i))
    return n_list


'''
def solution(n):
    return list(map(int, reversed(str(n))))
'''