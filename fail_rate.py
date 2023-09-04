#https://school.programmers.co.kr/learn/courses/30/lessons/42889



# 1. 일단 stages를 오름차순으로 정렬함
# 2. 2차원 배열인 fail_rate_list를 만들어 0번 인덱스에는 스테이지 번호, 1번 인덱스에는 클리어율을 담도록 한다
# 3 - 1. 만약 stages가 하나의 값으로 채워져 있다면 해당 스테이지의 클리어율을 1로 설정 후 스테이지 성공률을 내림차순하여 저장
# 3 - 2 일반적인 상황
#       stages 리스트가 빌 때 까지 반복한다.
#       무조건 현재 위치는 0번 인덱스가 되어야 한다
#       만약 0번 인덱스의 값이 스테이지의 총 수의 값보다 크면 모든 스테이지를 클리어 한 유저이므로 값을 삭제한다
#       그렇지 않을 시 해당 스테이지에 머무르고 있는 사람들을 list의 count를 사용하여 유저 수를 세고 fail_rate_list에 해당 스테이지 값에 클리어율을 지정한다
#       stages 리스트의 0~count번째 인덱스까지 삭제한다. 이를 계속 반복한다
# 4. 최종적으로 나온 fail_rate_list에 sort와 lambda를 사용해 첫번째로는 클리어율에 대한 내림차순을, 만약 첫번째에서 같은 값이 있을 경우 스테이지 순서 오름차순으로 지정한다 
def solution(N, stages):
    answer = []
    
    
    fail_rate_list = [[i+1,0] for i in range(N)]
    stages = sorted(stages)
    
    if len(set(stages)) == 1:
        if stages[0] > N : del stages[0]
        else:
            fail_rate_list[stages[0]-1][1] = 1
            fail_rate_list.sort(key = lambda x: (-x[1], x[0]))
            for i in fail_rate_list:
                answer.append(i[0])
            return answer
    
    
    
    while len(stages) > 0 :
        now_num = stages[0]
        if stages[0] > N : del stages[0]; continue
        count = stages.count(now_num)
        fail_rate_list[now_num-1][1] = count/len(stages)
        del stages[:count] 
            
        
        
    fail_rate_list.sort(key = lambda x: (-x[1], x[0]))
    
    for i in fail_rate_list:
        answer.append(i[0])
    
    return answer

print(solution(5,[6]))