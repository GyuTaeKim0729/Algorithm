def solution(n):
    answer = 0
    for i in range(1,n):
        if n % i == 1:
            answer = i
            break
    return answer


if __name__ == '__main__':
    n = 10
    result = 3
    solution_result = solution(n)
    print("Success" if result == solution_result else "Fail")
