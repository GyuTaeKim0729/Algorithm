def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


def solution2(absolutes, signs):
    answer = 0
    for absolute, sign in zip(absolutes, signs):
        if sign:
            answer += absolute
        else:
            answer -= absolute
    return answer


if __name__ == '__main__':
    absolutes = [4, 7, 12]
    signs = [True, False, True]
    result = 9
    solution_result = solution(absolutes, signs)
    print("Success" if result == solution_result else "Fail")
