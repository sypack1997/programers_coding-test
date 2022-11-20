def solution(n, times):
    left = 1
    right = max(times)*n # 가장 비효율적인 시간값
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time # mid 시간 내 심사를 받을 수 있는 인원 수
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            right = mid -1
        elif people < n:
            left = mid + 1
    return answer