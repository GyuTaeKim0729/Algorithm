def solution(N, M, data):
    answer = 0
    for i in data:
        temp = min(i)
        # answer = temp if answer < temp else answer
        answer = max(answer, temp)
    return answer


if __name__ == '__main__':
    result = 3
    N, M = 2, 4
    data = [[7, 3, 1,8], [3, 3, 3, 4]]
    solution_result = solution(N, M, data)
    print("Success" if result == solution_result else "Fail")
