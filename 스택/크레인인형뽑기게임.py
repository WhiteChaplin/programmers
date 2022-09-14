#https://school.programmers.co.kr/learn/courses/30/lessons/64061?language=python3
"""
초반에 멍청한 생각을 했다. 문제를 꼼꼼히 읽지 않고 푼 잘못인 거 같다
board의 컴마를 엔터를 입력해 가면서 배열을 만들었어야 했는데 그냥 봐서 그런지
0 0 0 4 3
0 0 2 2 5 
0 1 5 4 1   이렇게 봤다...개멍청했다
0 0 0 4 3
0 3 1 2 1
어쩐지 다 틀렸다고 뜨더라....
다시 배열을 바꾸어서 푸니 코드를 바꿔야 한다.
0은 비어있는 값을 뜻하니, 만약 특정 위치의 값이 0이 아니여서 값을 꺼냈다면 그 공간은 0으로 값을 바꾸면서 진행한다.

값을 꺼낸 것을 담는 get_list 리스트를 만든다.
get_list의 길이가 2 이상일 때
만약 get_list[-1]인 마지막값과  get_list[-2]인 마지막에서 두번째 값이 같다면
마지막에서 첫번째 두번째 값을 지우고
count를 2 올린다.

최종적으로 count를 반환하면 된다.

"""
def solution(board, moves):
    get_list = []
    count = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                get_list.append(board[j][i-1])
                board[j][i-1] = 0
                break
        if len(get_list) > 1 and get_list[-1] == get_list[-2]:
            get_list = get_list[:-2]
            count+=2

    return count

board = [[0,0,0,0,0],
         [0,0,1,0,3],
         [0,2,5,0,1],
         [4,2,4,4,2],
         [3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board,moves)