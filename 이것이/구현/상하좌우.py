def solution(N, data):
    answer = [1,1]

    for i in data:
        y,x = answer
        if i == 'L':
            x -= 1
        elif i == 'R':
            x += 1
        elif i == 'U':
            y -= 1
        elif i == 'D':
            y += 1
        if x != 0 and x != N+1:
            answer[1] = x
        if y != 0 and y != N+1:
            answer[0] = y

    return answer


if __name__ == '__main__':
    result = [3,4]
    solution_result = solution(5, ['R','R','R','U','D','D'])
    print("Success" if result == solution_result else "Fail")
