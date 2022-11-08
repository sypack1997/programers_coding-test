def solution(emergency):
    result = []
    for i in range(len(emergency)):
        cnt = 1
        for j in range(len(emergency)):
            if emergency[i] < emergency[j]:
                cnt += 1
        result.append(cnt)
    return result