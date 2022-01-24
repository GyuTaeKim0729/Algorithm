def solution(num):
    answer = 0
    while answer != 500 and num != 1:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        answer += 1
    return answer if answer != 500 else -1


if __name__ == '__main__':
    result = 8
    num = 6
    solution_result = solution(num)
    print("Success" if result == solution_result else "Fail")
