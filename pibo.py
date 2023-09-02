#https://school.programmers.co.kr/learn/courses/30/lessons/12945

#피보나치 수열은 재귀로 하면 값이 커질수록 횟수가 많아진다
#배열로 쉽게 하는 방법으로 하자

def solution(number):
    
    fibo_result = fibo(number)
    return fibo_result%1234567

def fibo(n):
    a,b = 1,1
    if n == 1 or n == 2: return 1
    
    for i in range(1,n):
        a,b = b, a+b
        
    return a


print(solution(3))