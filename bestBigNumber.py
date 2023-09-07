
#https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    str_numbers = []
    
    for i in numbers:
        str_numbers.append(str(i))
      
    #1000이하이기 때문에 3자리까지 적용
    str_numbers.sort(key=lambda x : x*3, reverse=True)
    
    
    return str(int(''.join(str_numbers)))

print(solution([3, 30, 5, 34, 9]))