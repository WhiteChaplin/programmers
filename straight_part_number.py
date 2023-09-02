#https://school.programmers.co.kr/learn/courses/30/lessons/131701

from collections import deque

# 시간초과
def solution(elements):
    num_list = []
    
    #i는 몇개씩 검사할 것인지
    for i in range(1,len(elements)+1):
        #j는 몇번 인덱스부터 검사할 것인지. 0~마지막 인덱스까지 돌면서 index 초과 시 빼면 된다
        for j in range(0,len(elements)):
            #k는 j 인덱스부터 i개씩 돌 때 사용
            sum = 0
            for k in range(i):
                # print(f"j : {j}, k : {k}")
                index = j+k
                # print(f"index : {index}")
                if index >= len(elements): 
                    index = index-len(elements)
                    print(index)
                    sum += elements[index]
                else:
                    sum += elements[index]
            # print(sum)
            if sum not in num_list : num_list.append(sum)
        # print()

    # print(sorted(num_list))
    # print(len(num_list))
    
    return len(num_list)

#--------------------------------------------------------------------------------------------------
#sum이랑 append가 굉장히 느린 작업인가보다
#일단 인덱싱 범위가 좁은 것을 방지하기 위해 elements를 한번 더 붙여서 out of range 해결
#sum과 슬라이싱을 이용해서 작업함


def answer(elements):
    result = set()
    
    eleLen = len(elements)
    elements = elements*2
    
    for i in range(eleLen):
        for j in range(eleLen):
            result.add(sum(elements[j:j+i+1]))

    return len(result)
    
print(answer([7,9,1,1,4]))