def solution(n):
    answer = ''
    if n % 2 == 0:
        answer += "수박" * int(n/2)
    else:
        answer += "수박" * int((n-1)/2)
        answer += "수"
    return answer

res = solution(1)
print(res)