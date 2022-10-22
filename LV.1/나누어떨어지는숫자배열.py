def solution(arr, divisor):
    arr_answer = []
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            arr_answer.append(arr[i])
    if len(arr_answer) == 0:
        arr_answer.append(-1)
    arr_answer.sort()
    return arr_answer


'''
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
'''