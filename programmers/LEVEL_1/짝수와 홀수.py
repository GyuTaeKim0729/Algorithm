def solution(num):
    return "Odd" if num % 2 != 0 else "Even"


if __name__ == '__main__':
    result = "Odd"
    num = 3
    solution_result = solution(num)
    print("Success" if result == solution_result else "Fail")
