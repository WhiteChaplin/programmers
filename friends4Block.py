#https://school.programmers.co.kr/learn/courses/30/lessons/17679

delete_list = []

def solution(m, n, boardList):
    same_str = ""
    board = []
    
    
    for i in range(len(boardList)):
        temp = []
        for j in range(len(boardList[0])):
            temp.append(boardList[i][j])
        board.append(temp)
            
            
    # print(board)
            
    for i in range(m-1):
        for j in range(n-1):
            same_count = 0
            pass_count = 0
            for k in range(i,i+2):
                for l in range(j,j+2):
                    if pass_count == 0: 
                        same_str = board[k][l]
                        # print(same_str)
                    # print(f"same str : {same_str}")
                    if board[k][l] == same_str:
                        # print(board[k][l])
                        same_count += 1
                    if same_count == 4:
                        # print(same_str)
                        if checkDuplicate(k-1,l-1) == False :delete_list.append([k-1,l-1])
                        if checkDuplicate(k-1,l) == False :delete_list.append([k-1,l])
                        if checkDuplicate(k,l-1) == False :delete_list.append([k,l-1])
                        if checkDuplicate(k,l) == False :delete_list.append([k,l])
                    pass_count += 1
            same_count = 0
            same_str = ""
            
            
            
            
    # newBoard = []
    if delete_list != [] : 
        # print(delete_list)
        for i in range(len(board)):
            board_str = ""
            for j in range(len(board[0])):
                # flag = False
                for (y,x) in delete_list:
                    if i == y and j == x: 
                        # board_str += "0"
                        board[i][j] = "0"
                        # flag = True
                        break
            # newBoard.append(board_str)
            
    print(board)
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "0":
                for innerI in range(i,len(board)):
                    # print(f"board : {board[j][innerI]}")
                    if board[j][innerI] != "0":
                        print(j)
                        # temp = board[i][j]
                        # print(temp)
                        # board[j][innerI] = temp
                        # board[j][innerI] = "0"
                        break
                    print()
    print(board)
                    
    
    
    
    # print(f"newboard : {newBoard}")
            # print(type(board[y][x]))
            # board[y][x] = "x"
            # print(board[y][x])
    
    
    
    
    answer = 0
    return answer

def checkDuplicate(x,y):
    global delete_list
    if(delete_list.count([x,y]) == 0) : return False
    
    return True

# solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
# solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])




"-----------------------------------------------------------------------------"
#문제 풀이 시간 초과로 인한 정답
#2x2의 내역들을 찾고 0으로 변경하는 거 까진 성공
#근데 밑으로 내리는 거에서 뭔가 꼬인듯 함

def check(m, n, board):
    
    #비어질 공간을 의미.
    filter = [[0 for _ in range(n)] for _ in range(m)]
    count = 0
    
    # check can delete
    for i in range(m-1):
        for j in range(n-1):
            #2x2 사각형
            a = board[i][j]
            b = board[i][j+1]
            c = board[i+1][j]
            d = board[i+1][j+1]
            if a == b == c == d and a != '0': #만약 4개가 모두 같다면
                filter[i][j], filter[i][j+1], filter[i+1][j], filter[i+1][j+1] = 1, 1, 1, 1
    
    #board에 삭제될 공간 적용
    for i in range(m):
        for j in range(n):
            if filter[i][j] == 1:
                count += 1
                board[i][j] = '0'
    
    #만약 더이상 삭제된 것이 없다면 0을 반환
    if count == 0:
        return 0
    
    # fill blank
    #빈 공간 채우기
    #제일 아래에서 2번째 행부터 체크한다. 제일 아래는 내려갈 공간이 없기 때문
    #m은 커질수록 아래로 향한다.
    for i in range(m-2, -1, -1):
        # print(i)
        for j in range(n):
            k = i
            while 0 <= k+1 < m and board[k+1][j] == '0':
                k += 1
                print(k)
            if k != i:
                board[k][j] = board[i][j]
                board[i][j] = '0'
                
    return count

def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        temp = check(m, n, board)
        if temp == 0:
            break
        answer += temp
        
    return answer

print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))