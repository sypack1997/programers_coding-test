def solution(num_list, n):
    result = []
    for i in range(0, len(num_list), n):
        result.append(num_list[i:i+n])
    return  result


'''
import numpy as np
def solution(num_list, n):
    li = np.array(num_list).reshape(-1, n)
    return li.tolist()
'''
# tolist : np형태의 array를 python형태의 list로 변환