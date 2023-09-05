#https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = [0]*len(prices)

    for i in range(len(prices)):
        for j in range(i,len(prices)-1):
            if prices[i] <= prices[j]: answer[i] += 1
            else: break

    return answer

print(solution([1,2,3,2,3]))