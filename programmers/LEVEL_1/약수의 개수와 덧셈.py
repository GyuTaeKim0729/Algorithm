def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if i ** 0.5 - int((i ** 0.5)) == 0.0:
            answer -= i
        else:
            answer += i
    return answer


def solution2(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += (-i if i ** 0.5 - int((i ** 0.5)) == 0.0 else i)
    return answer


if __name__ == '__main__':
    left = 13
    right = 17
    result = 43
    solution_result = solution2(left, right)
    print("Success" if result == solution_result else "Fail")
