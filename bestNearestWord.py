#https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = [-1]*len(s)
    
    wordList = {}
    
    for (index,value) in enumerate(s):
        if wordList.get(value) == None: wordList[value] = index
        else : answer[index] = index-wordList[value]; wordList[value] = index

  
    return answer

print(solution("banana"	))
