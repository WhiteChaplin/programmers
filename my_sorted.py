#https://school.programmers.co.kr/learn/courses/30/lessons/12915

#이거 예전에 풀어본 유형이었음
# 파이썬에서 정렬을 람다식으로 적용하면 1차적으로 어떻게 분류하고 만약 1차적인게 겹칠 시 2차적으로 분류할 수 있는 방법이 있음
def solution(strings, n):
    
    answer = []
    sorted_list = []
    
    for index in strings:
        sorted_list.append([index[n],index])
    
    
    sorted_list.sort(key = lambda x: (x[0], x[1]))
    
    
    for (_,string) in sorted_list:
        answer.append(string)
    
    return answer

print(solution(["abce", "abcd", "cdx"],2))