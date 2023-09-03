#https://school.programmers.co.kr/learn/courses/30/lessons/161989


#section의 다음 값들을 가져와서 현재 위치에 있는 값과 빼고 만약 그 값이 롤러의 range 내에 들어갈 경우 del_index를 높혀 section의 값을 삭제하면서 진행하였음
def solution(n, m, section):
    answer = 0
    
    section.sort()

    if m == 1: return len(section)
        
        
        
    while len(section) > 0:
        del_index = 1
        
        if len(section) > 1:
            for index in range(1,len(section)):
                if section[index]-section[0] < m:
                    del_index += 1
                else: break
            del section[:del_index]
            del_index = 0
            answer += 1
        else:
            del section[:1]
            answer += 1
            
    
    return answer

print(solution(5,4,[1, 3]))