#https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    eng_dict = {}
    
    turn = 0
    
    # print(eng_dict.get("hi"))
    
    for (index,word) in enumerate(words):
        if index%n == 0 : turn += 1
        
        if index > 0:
               if  word[0] != words[index-1][-1] : return [(index%n)+1,turn]
        
        if eng_dict.get(word) == None : eng_dict[word] = 1
        elif eng_dict.get(word) == 1 : return [(index%n)+1,turn]
        
        
        
            
    

    return [0,0]

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))