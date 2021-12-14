def solution(seoul):
    for i, v in enumerate(seoul):
        if v == 'Kim':
            return '김서방은 {}에 있다'.format(i)
            
        # print('index : {}, value : {}'.format(i,v))


seoul = ['Jane', 'Kim']
res = solution(seoul)
print(res)