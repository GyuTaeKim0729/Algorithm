def solution(n):
    temp = (n ** 0.5)
    return (temp+1) ** 2 if temp % 1 == 0.0 else -1


if __name__ == '__main__':
    result = 144
    n = 121
    solution_result = solution(n)
    print("Success" if result == solution_result else "Fail")
