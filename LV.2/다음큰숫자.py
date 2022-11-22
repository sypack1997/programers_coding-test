def solution(n):
    result = n + 1
    while True:
        if bin(n).count('1') == bin(result).count('1'):
            return result
            break
        else:
            result += 1