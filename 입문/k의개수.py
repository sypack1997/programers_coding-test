def solution(i, j, k):
    cnt = 0
    for num in range(i, j+1):
        num = str(num)
        for num_str in num:
            if str(k) == num_str:
                cnt += 1
    return cnt


'''
def solution(i, j, k):
    answer = sum([str(i).count(str(k)) for i in range(i, j+1)])
    return answer
'''