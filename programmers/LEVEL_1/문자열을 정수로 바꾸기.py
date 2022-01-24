def solution(s):
    answer = int(s)
    return answer


def solution2(s):
    answer = 0
    pm = 1

    for k in s:
        if k != '-' and k != '+':
            answer *= 10
            answer += ord(k) - ord('0')
        else:
            if k == '-':
                pm *= -1
    return answer * pm


if __name__ == '__main__':
    result = 1234
    s = "+1234"
    solution_result = solution2(s)
    print("Success" if result == solution_result else "Fail")
