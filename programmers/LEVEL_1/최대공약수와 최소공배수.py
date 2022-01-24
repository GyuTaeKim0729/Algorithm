def solution(n, m):
    answer = []
    a = n
    b = m
    while m > 0:
        temp = m
        m = n % m
        n = temp
    answer.append(n)
    answer.append(a * (b / n))
    return answer


if __name__ == '__main__':
    result = [3, 12]
    n = 3
    m = 12
    solution_result = solution(n, m)
    print("Success" if result == solution_result else "Fail")
