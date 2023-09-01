from collections import deque

#모든 노드에 있어서 +과 -을 둘다 적용해봐야함.
#재귀로 푸는 방법이 생각나서 재귀로 풀었음
# nonlocal로 밖의 함수나 전역변수를 자신이 있는 함수로 가지고 와 전역변수처럼 사용할 수 있다.



def solution(numbers, target):
    answer = 0
    
    def rec(index,targetNum):
        if index == len(numbers):
            if targetNum == target:
                nonlocal answer #answer를 전역으로 만듬
                answer += 1
            return
    
        else:
            rec(index+1, targetNum+numbers[index])
            rec(index+1, targetNum-numbers[index])
    
    rec(0,0)
    return answer

print(solution([1, 1, 1, 1, 1],3))