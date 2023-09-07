#https://school.programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    
    for i in range(len(numbers)):
        if i == len(numbers) : answer.add(numbers[i]); break
        
        for j in range(i+1,len(numbers)):
            answer.add(numbers[i]+numbers[j])
    
    return list(sorted(answer))

print(solution([1,1,1,1,1]))