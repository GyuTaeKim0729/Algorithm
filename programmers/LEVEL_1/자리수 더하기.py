def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n = n // 10
    return answer


def solution2(n):
    answer = sum([int(i) for i in str(n)])
    return answer


if __name__ == '__main__':
    result = 6
    n = 123
    solution_result = solution2(n)
    print("Success" if result == solution_result else "Fail")
