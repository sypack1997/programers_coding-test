def solution(phone_number):
    pn_list = list(phone_number)
    for i in range(0,len(pn_list)-4):
        pn_list[i] = '*'
    return (''.join(pn_list))

'''
def solution(phone_number):
    return '*' * (len(phone_number)-4) + phone_number[-4:]
'''