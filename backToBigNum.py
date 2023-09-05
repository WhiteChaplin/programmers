# https://school.programmers.co.kr/learn/courses/30/lessons/154539


# 앞에서부터 비교하니 굉장히 시간이 오래 걸려서 시간 초과 에러가 났음
# 그래서 중간중간마다 만약 기준 값보다 더 큰 값이 들어오게 되면 값을 적용하도록 하였음
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

print(solution([2,3,3,5]))