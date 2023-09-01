from collections import deque


#https://school.programmers.co.kr/learn/courses/30/lessons/87946
#DFS(깊이 우선 탐색)을 사용한 방법
# -> 첫 시작 노드는 모든 던전을 의미한다.
# -> 첫 노드들을 모두 방문하여 만약 현재 피로도가 입장 피도로보다 높고, 소모 되는 피로도를 뺐을 때 0보다 크면
#    해당 노드들을 need_visited에 넣는다
# -> need_visited를 사용하여 DFS를 반복한다
# -> need_visited를 popleft 한다. 이는 현재 피로도와 입장한 던전을 의미한다.
#    이 상태에서 모든 던전을 대입하고 가능한 던전만 need_visited에 append한다. 이때 i는 몇번 던전에 입장할 수 있는지에 대한 번호이다
#    만약 입장이 불가능한 던전은 더 이상 던전 진행이 불가능함으로 count에 방문한 노드들의 길이를 저장한다.
def solution(k, dungeons):
    count,need_visited = 0,deque()
    need_visited.append([k,[]])
    while need_visited:
        piro,visited_node=need_visited.popleft()
        print(visited_node)
        for i in range(len(dungeons)):
            [a,b]=dungeons[i]
            if i not in visited_node and piro>=a and piro-b>=1: need_visited.append([piro-b,visited_node+[i]])
            else : count=len(visited_node)
    return count

print(solution(80,[[80,20],[50,40],[30,10]]	))