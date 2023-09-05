#https://school.programmers.co.kr/learn/courses/30/lessons/49993#fnref1

def solution(skill, skill_trees):
    answer = 0
    
    
    for (index,value) in enumerate(skill_trees):
        skill_save = skill
        flag = True
        for i in value:
            if i in skill_save :
                if i == skill_save[0] : 
                    save_list = list(skill_save)
                    del save_list[0]
                    skill_save = ''.join(save_list)
                else: flag = False;break
            
        if flag : answer += 1
    
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))