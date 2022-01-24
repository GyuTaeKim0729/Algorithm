def solution(n):
    answer = n + 1 if n > 1 else n
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            answer += i
    return answer


if __name__ == '__main__':
    result = 1
    n = 1
    solution_result = solution(n)
    print("Success" if result == solution_result else "Fail")
