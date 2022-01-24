def solution(s):
    answer = 0
    for i in s.lower():
        if i == "p":
            answer += 1
        elif i == "y":
            answer -= 1
    return answer == 0


def solution2(s):
    return s.lower().count('p') == s.lower().count('y')


if __name__ == '__main__':
    result = True
    s = "pPoooyY"
    solution_result = solution2(s)
    print("Success" if result == solution_result else "Fail")
