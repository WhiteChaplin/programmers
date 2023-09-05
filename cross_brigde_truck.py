#https://school.programmers.co.kr/learn/courses/30/lessons/42583
#트럭 1대당 1초에 1 bridge_length 만큼 이동한다.
#tc 2번은 1초에 트럭이 적재되고 length가 100이라서 return이 101
#tc 3번은 lenght가 100이고 10개의 트럭이 동시에 올라가는 것이 가능하다. 근데 무조건 1초 딜레이가 존재하기 때문에
#실질적으로 걸리는 시간은 트럭 1대당 11초이며 10대가 지나갔으니 110초가 할애된다.



#진짜 어떻게 풀어야하는지 감이 안잡혀서 정답 참고함
# 실제로 다리를 deque를 사용해서 만드는 것이 좋음

# 다리의 모든 값이 제거될 때 까지 반복함
# 반복 시 왼쪽에 있는 값을 pop하여 시간이 지나 한칸 이동했다는 것을 표현함. 그리고 1초가 지났다는 의미로 answer를 1 올림
# 해당 위치에 있는 트럭의 무게를 전체 무게에서 뺌. 만약 없다면 0이 빠짐

# 만약 남아있는 트럭들이 있을 때 남아있는 트럭의 무게를 합한 것이 최대 부하할 수 있는 무게보다 작거나 같으면 다리의 트럭 값을 추가함
# 무게가 크면 0을 추가하여 트럭이 올라오지 못함을 의미함

# 다리 리스트의 모든 값이 사라질 떄 까지 반복


# sum(list)는 시간이 굉장히 오래 소요되는 작업이기에 차라리 변수를 하나 만들어서 sum의 값을 미리 담을 수 있는 변수를 지정하는 것이 좋음
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weight_list = deque([0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    
    while truck_weight_list:
        
        answer += 1
        remove = truck_weight_list.popleft()
        bridge_weight -= remove
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge_weight += truck
                truck_weight_list.append(truck)    
            else:
                truck_weight_list.append(0)
        
        
    return answer

print(solution(2,10,[7,4,5,6]))