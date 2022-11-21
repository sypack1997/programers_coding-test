def solution(participant, completion):
    part = sorted(participant)
    com = sorted(completion)
    
    for i in range(len(com)):
        if part[i] != com[i]:
            return part[i]
    
    return part[-1]


'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''