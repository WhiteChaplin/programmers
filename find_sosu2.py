#https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import combinations,permutations

def solution(numbers):
    answer = 0
    
    num_dict = {}
    
    for i in range(1, len(numbers)+1):
        input_list = list(permutations(numbers,i))
        for input in input_list:
            if is_prime(int(''.join(input))) == True and num_dict.get(int(''.join(input))) == None: 
                num_dict[int(''.join(input))] = 1
                answer += 1
    
    return answer


def is_prime(number):
    if number == 2 or number == 3 : return True
    if number % 2 == 0 or number < 2 : return False
    root = int(number**0.5+1)
    for i in range(2,root):
        if number % i == 0 : return False
    return True


print(solution("17"))