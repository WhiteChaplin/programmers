#https://school.programmers.co.kr/learn/courses/30/lessons/42888
# 1트컷!
def solution(record):
    answer = []
    
    do_list = []
    dict_id = {}
    for index in record:
        do_list.append([index.split(" ")[0],index.split(" ")[1]])
        if len(index.split(" ")) > 2 : dict_id[index.split(" ")[1]] = index.split(" ")[2]
    # print(do_list)
    # print(dict_id)
    
    for (doing,uid) in do_list:
        if doing == "Enter":
            answer.append(f"{dict_id[uid]}님이 들어왔습니다.")
        elif doing == "Leave":
            answer.append(f"{dict_id[uid]}님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))