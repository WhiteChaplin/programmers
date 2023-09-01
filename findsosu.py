#https://school.programmers.co.kr/learn/courses/30/lessons/92335

answer = 0

def solution(n, k):
    
    
    jinsu = getJinsu(n,k)

    print(jinsu)
    
    if len(jinsu) == 1:
        if int(jinsu) == 0 : return 0
        else: return 1
    
    if(countP(jinsu) == 1): return 1
    
    count0P0(jinsu)
    countP0(jinsu)
    count0P(jinsu)
    return answer
    

def getJinsu(n,k):
    strJinsu = ""
    number = n
    div = k
    while number > div:
        strJinsu += str(number%div)
        number = number//div
    
    strJinsu += str(number%div)
    
    strJinsu = list(strJinsu)
    strJinsu.reverse()
    strJinsu = ''.join(strJinsu)
    return str(strJinsu)

def countP(jinsuStr):
    target = jinsuStr
    if target.find("0",0) == -1:
        if is_prime(float(target)) == True:
            return 1
    else: return 0
    
    

def count0P0(jinsuStr):
    target = ""
    for index in range(len(jinsuStr)):
        if jinsuStr[index] == "0":
            for inner in range(index, len(jinsuStr)):
                target += jinsuStr[inner]
                if index != len(jinsuStr)-1 and jinsuStr[index+1] == "0": break
                # print(f"0p0 : {target}")
                if(target[0] == "0" and target[len(target)-1] == "0" and len(target) > 2):
                    if is_prime(float(target[1:len(target)-1])) == True : 
                        # print(f"0p0 : {target}")
                        global answer
                        answer += 1
                    target = ""
                    break
                if(inner == len(jinsuStr)): target = ""
                

                
def countP0(jinsuStr):
    target = ""
    startIndex = 0
    for index in range(len(jinsuStr)):
        target += jinsuStr[index]
        if jinsuStr[index] == "0":
            # print(f"startindex : {startIndex}")
            if len(target) > 1 and target[len(target)-1] == "0" and jinsuStr[startIndex] != "0":
                if is_prime(float(target[:len(target)-1])) == True:
                    # print(f"p0 : {target}")
                    global answer; answer += 1
                target = ""
                startIndex = index
                
def count0P(jinsuStr):
    target = ""
    for index in range(len(jinsuStr)-1,0,-1):
        if jinsuStr[index] == '0':
            for inner in range(index+1,len(jinsuStr)):
                target += jinsuStr[inner]
            if target != "" and is_prime(float(target)) == True:
                # print(f"0p : {target}")
                global answer; answer += 1 
            break
                
def is_prime(number):
    if number == 2 or number == 3: return True  # 2 or 3 은 소수
    if number % 2 == 0 or number < 2: return False  # 2의 배수이거나 2보다 작은 값인 경우 소수가 아님
    root = int(number ** 0.5 +1)
    for i in range(2,root):
        if number % i == 0: return False
    return True    

print(solution(536345,8))