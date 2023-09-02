#https://school.programmers.co.kr/learn/courses/30/lessons/136798


def solution(number, limit, power):
    answer = 0
    
    for i in range(1,number+1):
        powerLevel = yaksu(i)
        # print(powerLevel)
        if powerLevel > limit: powerLevel = power
        
        answer += powerLevel
    
    return answer

#약수 구하는 알고리즘
def yaksu(n):
    
    yaksuList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            yaksuList.append(i) 
            if ( (i**2) != n) : 
                yaksuList.append(n // i)

    # yaksuList.sort()
    
    return len(yaksuList)

print(solution(5,3,2))