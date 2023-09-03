#https://school.programmers.co.kr/learn/courses/30/lessons/67256


left_keypad = [1,4,7]
right_keypad = [3,6,9]
center_keypad = [2,5,8,0]

def solution(numbers, hand):
    answer = ''
    left_hand_loc = 3
    right_hand_loc = 3
    do_left_center = False
    do_right_center = False
    
    for i in numbers:
        print(i)
        if i in left_keypad : answer+="L"; left_hand_loc = left_keypad.index(i); do_left_center = False
        elif i in right_keypad : answer += "R"; right_hand_loc = right_keypad.index(i); do_right_center = False
        elif i in center_keypad :
            num_loc = center_keypad.index(i)
            # print(abs(left_hand_loc-num_loc), abs(right_hand_loc-num_loc), i)

            if do_left_center == True and do_right_center == True:
                if abs(left_hand_loc-num_loc) > abs(right_hand_loc-num_loc) : answer += "R"; right_hand_loc = num_loc
                elif abs(left_hand_loc-num_loc) == abs(right_hand_loc-num_loc) : 
                    answer += hand[0].upper()
                    if hand[0] == "l" : left_hand_loc = num_loc
                    elif hand[0] == "r" : right_hand_loc = num_loc
                else: answer += "L"; left_hand_loc = num_loc
            
            elif do_left_center:
                if abs(left_hand_loc-num_loc) > abs(right_hand_loc-num_loc)+1 : answer += "R"; right_hand_loc = num_loc; do_right_center = True
                elif abs(left_hand_loc-num_loc) == abs(right_hand_loc-num_loc)+1 : 
                    answer += hand[0].upper()
                    if hand[0] == "l" : left_hand_loc = num_loc; do_left_center = True
                    elif hand[0] == "r" : right_hand_loc = num_loc; do_right_center = True
                else: answer += "L"; left_hand_loc = num_loc; do_left_center = True
                
            elif do_right_center:
                if abs(left_hand_loc-num_loc)+1 > abs(right_hand_loc-num_loc) : answer += "R"; right_hand_loc = num_loc; do_right_center = True
                elif abs(left_hand_loc-num_loc)+1 == abs(right_hand_loc-num_loc) : 
                    answer += hand[0].upper()
                    if hand[0] == "l" : left_hand_loc = num_loc; do_left_center = True
                    elif hand[0] == "r" : right_hand_loc = num_loc; do_right_center = True
                else: answer += "L"; left_hand_loc = num_loc; do_left_center = True
                
            
            else:
                if abs(left_hand_loc-num_loc) > abs(right_hand_loc-num_loc) : answer += "R"; right_hand_loc = num_loc; do_right_center = True
                elif abs(left_hand_loc-num_loc) == abs(right_hand_loc-num_loc) : 
                    answer += hand[0].upper()
                    if hand[0] == "l" : left_hand_loc = num_loc; do_left_center = True
                    elif hand[0] == "r" : right_hand_loc = num_loc; do_right_center = True
                else: answer += "L"; left_hand_loc = num_loc; do_left_center = True
            
    
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))