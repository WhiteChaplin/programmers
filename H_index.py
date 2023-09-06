#https://school.programmers.co.kr/learn/courses/30/lessons/42747


from collections import Counter
def solution(citations):
    answer = 0
    count_dict = dict(Counter(sorted(citations)))
    if max(citations) == 0 : return 0
    if len(citations) == 1 : return 1
    
    
    for i in range(1,max(citations)+1):
        count = 0
        for (key,value) in count_dict.items():
            if key >= i: 
                count += value
                if count >= i:
                    answer = i

    
    
    return answer


# print(solution([1,1,1,1]))
print(solution([3,0,6,1,5]))