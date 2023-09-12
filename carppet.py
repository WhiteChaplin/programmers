#https://school.programmers.co.kr/learn/courses/30/lessons/42842


def getYaksu(n):
    
    yaksuList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            yaksuList.append([i,n//i]) 
    yaksuList.sort()
    
    return yaksuList


def solution(brown, yellow):
    
    total = brown+yellow
    yaksu_list = getYaksu(total)
    
    for (x,y) in yaksu_list:
        if brown == ( ((x*2)-1) + ((y*2)-3) ) : 
            if y > x : return[y,x]
            else : return [x,y]
        elif brown == ( ((y*2)-1) + ((x*2)-3) ) : 
            if y > x : return[y,x]
            else : return [x,y]


print(solution(10,2))