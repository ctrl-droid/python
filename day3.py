# 수박수박수박수박수박수?
'''
길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
'''
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