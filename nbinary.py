#https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    number = 0
    turn = 1
    
    while len(answer) < t:
        my_turn = p%m

        if number >= n:
            convert = convert_notation(number,n)
            for i in convert:
                if turn%m == my_turn:
                    answer += i
                    if len(answer) == t : return answer
                turn += 1
                    
            
        else:
            convert = convert_notation(number,n)
            for i in convert:
                if turn%m == my_turn:
                    answer += i
                    if len(answer) == t : return answer
                turn += 1
                
                    
            
        number += 1

    
    return answer
    
#n진수 구하는 방법
def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    
    #q가 0보다 크면 재귀 실행, 아니면 T의 문자열에 자리에 해당하는 값 반환
    return convert_notation(q, base) + T[r] if q else T[r]    


print(solution(2,4,2,1))