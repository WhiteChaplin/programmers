#https://school.programmers.co.kr/learn/courses/30/lessons/92341

import math
def solution(fees, records):
    answer = []
    parking_dict = {}
    
    for index in records:
        # print(int(index[:2]), index[3:5], index[6:10], index[11:])
        if parking_dict.get(index[6:10]) == None:
            parking_dict[index[6:10]] = [int(index[:2]),int(index[3:5]),index[11:],0]
            
            
        elif index[11:] == "IN":
            value = parking_dict[index[6:10]]
            parking_dict[index[6:10]] = [int(index[:2]),int(index[3:5]), "IN", value[3] ]
        
        elif index[11:] == "OUT":
            
            value = parking_dict[index[6:10]]
            
            parking_dict[index[6:10]] = [int(index[:2]),int(index[3:5]), "None", value[3] + ( int(index[:2])*60 + int(index[3:5]) - (value[0]*60 + value[1]) ) ]
            
            
    for (key,value) in parking_dict.items():
        if value[2] =="IN":
            parking_dict[key] = [23,59, "None", value[3] + ( 23*60 + 59) - (value[0]*60 + value[1])]
    
    
    parking_dict = sorted(parking_dict.items(), key=lambda x : x[0])
    
    for (key,value) in parking_dict:
        pay = 0
        time = value[3]
        if time >= fees[0]: 
            pay += fees[1] 
            time -= fees[0]

            pay += math.ceil(time/fees[2])*fees[3]
            answer.append(pay)
        else : answer.append(fees[1])
    

    return answer

print(solution([120, 0, 60, 591],
         ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))