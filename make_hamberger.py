#https://school.programmers.co.kr/learn/courses/30/lessons/133502
from collections import deque

def solution1(ingredient):
    answer = 0
    range_list=[]
    before = 0
    
    ing_list = deque(ingredient)
    
    while True:
        
        for i in range(len(ing_list)):
            if ing_list[i] == 1:
                if before == 3:
                    range_list.append(i)
                    before = 0
                    break
                else:
                    range_list = []
                    range_list.append(i)
                    before = 1
                
            elif ing_list[i] == 2:
                if before == 1:
                    range_list.append(i)
                    before = 2
                else: 
                    range_list = []
                    before = 0
                
            elif ing_list[i] == 3:
                if before == 2:
                    range_list.append(i)
                    before = 3
                else: 
                    range_list = []
                    before = 0
            
        if len(range_list) == 4:
            for index in range_list:
                ing_list[index] = 0
            
            ing_list = [i for i in ing_list if i != 0]
            answer += 1
        
        else: break
    
    return answer


#-------------------------------------------------------------------------------
# 시간 에러가 나서 ingredient를 문자로 변경하고 replace를 사용하는 방법으로 시도
# 하지만 왜인지 몇개에 있어서 실패가 나옴.
# 알았다. replace는 전체 문자열에서 해당 문자열을 찾음
# 반례로 1,2,1,2,3,1,3,1,2,3,1 를 하면 1,2,1,2,3,1 -> 이거로 하나 빠진 후 1,2,3,1,2,3,1에서 1,2,3,1이 빠진다고 생각을 했으나
# 실제로는 1,2,3,1을 무조건 다 찾아버려서 중간의 1,2,3,1과 맨 뒤에 1,2,3,1이 체킹되어 버림
# 문제의 관점으로 봤을 때 1,2,3,1이 모이는 순간 삭제시키는 것이 맞기 때문에 마지막 방법으로 푼 방법이 맞음.
def solution2(ingredient):
    ing_str = []
    answer = 0
    
    for i in ingredient:
        ing_str.append(str(i))
    
    ing_str = ''.join(ing_str)
    
    while True:
        beforeLen = len(ing_str)
        repeat = ing_str.count("1231")
        print(f"before replace : {ing_str}")
        ing_str = ing_str.replace("1231","",repeat)
        print(f"after replace : {ing_str}")
        answer += repeat
        if beforeLen == len(ing_str) : break
        
    
    return answer


#------------------------------------------------------------------
#마지막 방법. 아까는 앞에서 셌으니 뒤에서 세는게 좋아보임
# 특정 list에 하나씩 값을 담고 마지막 4개의 값이 1,2,3,1 이면 리스트 삭제하고 answer에 값 추가
# 이렇게 하니까 되네;
def solution(ingredient):
    answer = 0
    ing_list = []
    
    for i in ingredient:
        ing_list.append(i)
        
        if ing_list[-4:] == [1,2,3,1]:
            del ing_list[-4:]
            answer += 1
    
    

print(solution2([1,2,1,2,3,1,3,1,2,3,1]))