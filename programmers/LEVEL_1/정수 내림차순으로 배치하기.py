def solution(n):
    answer = 0
    temp = sorted((str(n)), reverse=True)
    for k in temp:
        answer *= 10
        answer += int(k)
    return answer


def solution2(n):
    return int("".join(sorted((str(n)), reverse=True)))


def solution3(n):
    answer = 0
    temp = sorted((str(n)), reverse=True)
    answer = int("".join(temp))
    return answer


if __name__ == '__main__':
    result = 873211
    n = 118372
    solution_result = solution2(n)
    print("Success" if result == solution_result else "Fail")
