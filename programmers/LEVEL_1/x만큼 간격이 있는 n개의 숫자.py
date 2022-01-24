def solution(x, n):
    return [x * i + x for i in range(n)]


if __name__ == '__main__':
    result = [2, 4, 6, 8, 10]
    x = 2
    n = 5
    solution_result = solution(x, n)
    print("Success" if result == solution_result else "Fail")
