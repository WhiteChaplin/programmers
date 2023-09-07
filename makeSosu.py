#https://school.programmers.co.kr/learn/courses/30/lessons/12977
#https://velog.io/@sloools/Python-%EC%88%9C%EC%97%B4Permutation-%EC%A1%B0%ED%95%A9Combination 순열 조합에 대한 내용
# 조합은 자주 나오는 유형으로 꼭 알고 있기
from itertools import combinations, permutations
def solution(nums):
    answer = 0


    combi = list(combinations(nums,3))
    
    
    for i in combi:
        if is_prime(sum(i)) == True: answer+=1

    return answer

def is_prime(number):
    if number == 2 or number == 3: return True  # 2 or 3 은 소수
    if number % 2 == 0 or number < 2: return False  # 2의 배수이거나 2보다 작은 값인 경우 소수가 아님
    root = int(number ** 0.5 +1)
    for i in range(2,root):
        if number % i == 0: return False
    return True  


print(solution([1,2,7,6,4]))