def solution(n, a, b):
    answer = 0
    while True:
        if (a == b + 1 and a % 2 == 0) or (a + 1 == b and a % 2 != 0):
            answer += 1
            break
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1
    return answer


if __name__ == '__main__':
    result = 3
    n = 8
    a = 1
    b = 7
    solution_result = solution(n, a, b)
    print("Success" if result == solution_result else "Fail")
