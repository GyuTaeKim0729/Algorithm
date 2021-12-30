def solution(a, b):
    answer = 0
    for a_one, b_one in zip(a, b):
        answer += a_one*b_one
    return answer


def solution2(a, b):
    return sum([x*y for x,y in zip(a, b)])


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]
    result = 3
    solution_result = solution(a, b)
    print("Success" if result == solution_result else "Fail")
