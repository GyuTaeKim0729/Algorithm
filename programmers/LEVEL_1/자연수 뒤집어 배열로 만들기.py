def solution(n):
    answer = []
    while n:
        answer.append(n % 10)
        n = n // 10
    return answer


if __name__ == '__main__':
    result = [1]
    n = 1
    solution_result = solution(n)
    print("Success" if result == solution_result else "Fail")
