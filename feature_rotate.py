#https://school.programmers.co.kr/learn/courses/30/lessons/76502


def solution1(s):
    answer = 0
    
    s_count = 0
    m_count = 0
    l_count = 0
    
    def checkState(strs):
        
        nonlocal s_count
        nonlocal m_count
        nonlocal l_count
        
        openS = None
        endS = None
        openM = None
        endM = None
        openL = None
        endL = None
        
        
        
        strs = list(strs)
        
        flag = True
        
        for i in strs:
            if i == "(" :
                if endS == True :
                    return False
                elif openS == True : s_count += 1
                else : openS = True; s_count += 1
            if i == ")" : 
                if openS == None : return False
                if s_count > 0 :
                    endS = None
                    openS = True
                    s_count -= 1
                else:
                    endS = None
                    openS = None
            if i == "{" : 
                if endM == True : return False
                elif openM == True : m_count += 1
                else : openM = True; m_count += 1
            if i == "}" : 
                if openM == None : return False
                if m_count > 0 :
                    endM = None
                    openM = True
                    m_count -= 1
                else:
                    endM = None
                    openM = None
            if i == "[" : 
                if endL == True : return False
                elif openL == True : l_count += 1
                else : openL = True; l_count += 1
            if i == "]" : 
                if openL == None : return False
                if l_count > 0 :
                    endL = None
                    openL = True
                    l_count -= 1
                else:
                    openL = None
                    endL = None

            # print(f"s_count : {s_count} / m_count : {m_count} / l_count : {l_count} / str : {i}")
            # print()
            
        if s_count == 0 and m_count == 0 and l_count == 0: return True
        
        return False

    
    sLen = len(s)
    s = s*2
    
    for i in range(sLen):
        strs = s[i:i+sLen]
        # print()
        if strs[0] == ")" or strs[0] == "}" or strs[0] == "]" : continue
        elif checkState(strs) == True : answer += 1
        
        
            
    return answer


#---------------------------------------------------------------------------------
# 올바른 괄호 문자열이라는 건 지우다보면 모든 값들을 지울 수 있다는 것
# 그래서 replace를 사용하여 만약 문자열을 모두 지울 수 있다면 값을 증가시키면 된다

def solution(s):
    answer = 0
    sLen = len(s)
    s = s*2 #한칸씩 옮기기 위해 문자열의 길이를 2배로 늘리고 칸을 이동하는 방법으로 진행
    for i in range(sLen):
        strs = s[i:i+sLen]
        while True:
            strsLen = len(strs)
            strs = strs.replace("()","")
            strs = strs.replace("{}","")
            strs = strs.replace("[]","")
            
            if len(strs) == 0:
                answer += 1
                break
            
            if len(strs) == strsLen: break
            
    return answer

print(solution("[]({(){}[]})"))